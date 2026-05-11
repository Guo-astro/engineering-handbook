#!/usr/bin/env node
/**
 * update-frontmatter-dates.mjs
 *
 * Bumps the `date_updated` field in the YAML frontmatter of content files
 * whose paths are passed as CLI arguments. Designed to be called from a
 * git pre-commit hook with the list of staged files.
 *
 * Usage:
 *   node scripts/update-frontmatter-dates.mjs <path> [<path> ...]
 *
 * Behavior:
 *   - Only acts on files under `content/` ending in `.md`.
 *   - Skips files with no YAML frontmatter.
 *   - Skips files whose `date_updated` is already today's date (idempotent,
 *     so re-running is cheap and does not create noise commits).
 *   - Adds `date_updated: YYYY-MM-DD` as the last frontmatter field if it
 *     is missing.
 *   - Writes the updated file and emits each updated path on stdout so
 *     the caller can `git add` them back.
 *
 * Escape hatches:
 *   - `HLD_SKIP_DATE_UPDATE=1` env var: exits 0 without doing anything.
 *   - `git commit --no-verify` bypasses the hook entirely.
 *
 * Exit codes:
 *   0 - success (zero or more files updated)
 *   1 - one or more target files could not be read / written / parsed
 *   2 - invalid invocation (no paths, bad args)
 */

import { readFile, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { argv, exit, stdout, stderr, env } from 'node:process';
import { resolve, relative, sep } from 'node:path';

// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------

const CONTENT_DIR = 'content';
const FRONTMATTER_DELIMITER = '---';

// Fields that, when changed, should trigger a date_updated bump. We accept
// ANY change under content/ by default; this list is informational and can
// be tightened later if we see too-frequent date churn on purely formatting
// commits.

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/** Returns today's date as YYYY-MM-DD in local time. */
function today() {
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  return `${yyyy}-${mm}-${dd}`;
}

/**
 * Returns true if the given path sits inside `content/` (not `content-old/`,
 * not `reports/`, etc.) and ends with `.md`.
 */
function isContentMarkdown(relativePath) {
  const normalised = relativePath.split(sep).join('/');
  return normalised.startsWith(`${CONTENT_DIR}/`) && normalised.endsWith('.md');
}

/**
 * Splits a markdown file into (frontmatterBody, bodyAfter) where
 * frontmatterBody is the YAML text between the opening and closing `---`,
 * and bodyAfter is everything after the closing `---` (including its
 * trailing newline). Returns null if the file has no frontmatter.
 */
function splitFrontmatter(raw) {
  if (!raw.startsWith(FRONTMATTER_DELIMITER)) {
    return null;
  }
  // Find the closing delimiter. It must sit at column 0 on its own line.
  const lines = raw.split('\n');
  if (lines[0].trim() !== FRONTMATTER_DELIMITER) {
    return null;
  }
  let closeIdx = -1;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === FRONTMATTER_DELIMITER) {
      closeIdx = i;
      break;
    }
  }
  if (closeIdx === -1) {
    return null;
  }
  const frontmatterLines = lines.slice(1, closeIdx);
  const bodyLines = lines.slice(closeIdx + 1);
  return {
    frontmatter: frontmatterLines.join('\n'),
    body: bodyLines.join('\n'),
    // Preserve whether the file ended with a trailing newline.
    trailingNewline: raw.endsWith('\n'),
  };
}

/**
 * Updates (or inserts) the `date_updated` field in the given frontmatter
 * text. Returns the new frontmatter text, or null if no change was needed.
 * The function preserves quoting style when the field already exists.
 */
function updateDateUpdated(frontmatter, dateStr) {
  const lines = frontmatter.split('\n');
  const pattern = /^(\s*date_updated\s*:\s*)(['"]?)([^'"\s#]+)\2(\s*(?:#.*)?)$/;

  let found = false;
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(pattern);
    if (m) {
      const [, prefix, quote, currentValue, suffix] = m;
      if (currentValue === dateStr) {
        // Already up to date; no change needed.
        return null;
      }
      lines[i] = `${prefix}${quote}${dateStr}${quote}${suffix}`;
      found = true;
      break;
    }
  }

  if (!found) {
    // Append at the end of the frontmatter block, just before the closing ---.
    lines.push(`date_updated: ${dateStr}`);
  }

  return lines.join('\n');
}

/**
 * Processes a single file path. Returns 'updated' | 'skipped' | 'error'.
 * Prints error details to stderr on failure.
 */
async function processFile(relPath, dateStr) {
  const absPath = resolve(relPath);
  if (!existsSync(absPath)) {
    // File was staged-for-delete. Skip silently.
    return 'skipped';
  }

  let raw;
  try {
    raw = await readFile(absPath, 'utf8');
  } catch (err) {
    stderr.write(`[date-update] Failed to read ${relPath}: ${err.message}\n`);
    return 'error';
  }

  const parts = splitFrontmatter(raw);
  if (!parts) {
    // No frontmatter (or malformed); leave it alone.
    return 'skipped';
  }

  const newFrontmatter = updateDateUpdated(parts.frontmatter, dateStr);
  if (newFrontmatter === null) {
    // Already today's date. Idempotent skip.
    return 'skipped';
  }

  const rebuilt =
    `${FRONTMATTER_DELIMITER}\n${newFrontmatter}\n${FRONTMATTER_DELIMITER}\n${parts.body}${parts.trailingNewline && !parts.body.endsWith('\n') ? '\n' : ''}`;

  try {
    await writeFile(absPath, rebuilt, 'utf8');
  } catch (err) {
    stderr.write(`[date-update] Failed to write ${relPath}: ${err.message}\n`);
    return 'error';
  }

  return 'updated';
}

// ---------------------------------------------------------------------------
// Entry point
// ---------------------------------------------------------------------------

async function main() {
  if (env.HLD_SKIP_DATE_UPDATE === '1') {
    // Honoured escape hatch for callers that explicitly want to skip.
    exit(0);
  }

  const paths = argv.slice(2);
  if (paths.length === 0) {
    // No paths given. Not an error; simply a no-op.
    exit(0);
  }

  const dateStr = today();
  const cwd = process.cwd();

  let errors = 0;
  const updated = [];

  for (const p of paths) {
    const rel = relative(cwd, resolve(p));
    if (!isContentMarkdown(rel)) {
      continue;
    }
    const result = await processFile(rel, dateStr);
    if (result === 'error') errors += 1;
    if (result === 'updated') updated.push(rel);
  }

  // Emit each updated path on a single line so the caller can `git add` them.
  for (const p of updated) {
    stdout.write(`${p}\n`);
  }

  exit(errors === 0 ? 0 : 1);
}

main().catch((err) => {
  stderr.write(`[date-update] Unexpected error: ${err.stack || err}\n`);
  exit(1);
});
