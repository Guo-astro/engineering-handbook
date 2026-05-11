#!/usr/bin/env node
/**
 * Validates YAML frontmatter on every Markdown file under content/.
 * Usage: node scripts/check-frontmatter.mjs
 */

import { readFile, glob } from 'node:fs/promises';
import { exit } from 'node:process';

const REQUIRED_FIELDS = [
  'title',
  'description',
  'part',
  'module',
  'difficulty',
  'prerequisites',
  'date_created',
  'date_updated',
];

// Trade-off pages live outside the 12-part curriculum and use a simpler schema.
const TRADEOFF_REQUIRED_FIELDS = ['title', 'description', 'related'];

const VALID_DIFFICULTY = ['beginner', 'intermediate', 'advanced'];

// Canonical tag vocabulary. Keep in sync with STYLE_GUIDE.md "Canonical tags".
// `tags:` is for topic concepts. Tool names live in `technologies:` instead.
const VALID_TAGS = new Set([
  // Distributed systems
  'consistency', 'replication', 'partitioning', 'consensus', 'transactions',
  'idempotency', 'fanout',
  // Data storage
  'sql', 'nosql', 'cache', 'storage-engines', 'vector-search', 'time-series',
  'search', 'geospatial',
  // Messaging
  'queue', 'stream-processing', 'cdc',
  // Networking
  'http-api', 'real-time', 'cdn', 'dns', 'load-balancing',
  // Architecture
  'microservices', 'event-driven', 'serverless', 'api-gateway', 'multi-tenant',
  // Traffic
  'rate-limiting', 'identifier',
  // Reliability
  'observability', 'resilience', 'deployment', 'slo',
  // Security
  'authn-authz', 'encryption', 'zero-trust',
  // AI / ML
  'llm', 'rag', 'ml-systems', 'ai-safety', 'agents',
  // Media
  'video',
  // Cross-cutting
  'cost',
]);

// Part 8 case-study themes. Purely editorial grouping: never affects URLs, the
// numbered Part 8 curriculum position, or cross-references. Adding a new value
// here is the only step needed to introduce a new theme bucket.
const VALID_CASE_STUDY_THEMES = [
  'core-primitives',
  'consumer-products',
  'ai-systems',
  'financial-systems',
  'infrastructure-platforms',
];

// Lazy-load the technology allowlist; a missing/malformed file is non-fatal
// and simply disables technology validation.
let ALLOWED_TECHNOLOGIES = null;
try {
  const raw = await readFile(new URL('./technologies.json', import.meta.url), 'utf8');
  const parsed = JSON.parse(raw);
  if (Array.isArray(parsed.allowed)) {
    ALLOWED_TECHNOLOGIES = new Set(parsed.allowed);
  }
} catch {
  ALLOWED_TECHNOLOGIES = null;
}

let errorCount = 0;
let fileCount = 0;

// Registry keys look like "1.3-consistency-models" — part.idx-slug where idx
// is NOT zero-padded (matches the prerequisites: slug format in STYLE_GUIDE.md).
const MODULE_REGISTRY = new Set();

const stripQuotes = (s) => s.replace(/^["']|["']$/g, '');

function registerModule(file) {
  const m = file.match(/content\/part-(\d+)-[^/]+\/(\d+)-([^/]+)\.md$/);
  if (!m) return;
  const [, part, idx, slug] = m;
  MODULE_REGISTRY.add(`${part}.${parseInt(idx, 10)}-${slug}`);
}

function parseFrontmatter(contents, file) {
  const match = contents.match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    console.error(`\u274c ${file}: no YAML frontmatter block found`);
    return null;
  }

  const obj = {};
  let currentArrayKey = null;

  for (const line of match[1].split('\n')) {
    if (!line.trim() || line.trim().startsWith('#')) continue;

    if (line.match(/^\s+- /)) {
      if (!currentArrayKey) continue;
      obj[currentArrayKey].push(stripQuotes(line.replace(/^\s+- /, '').trim()));
      continue;
    }

    const m = line.match(/^([a-z_]+):\s*(.*)$/);
    if (!m) continue;
    const [, key, rawValue] = m;
    const trimmedRaw = rawValue.trim();

    const inlineArray = trimmedRaw.match(/^\[(.*)\]$/);
    if (inlineArray) {
      const inner = inlineArray[1].trim();
      obj[key] = inner === ''
        ? []
        : inner.split(',').map((s) => stripQuotes(s.trim())).filter((s) => s.length > 0);
      currentArrayKey = null;
    } else if (trimmedRaw === '') {
      obj[key] = [];
      currentArrayKey = key;
    } else {
      obj[key] = stripQuotes(trimmedRaw);
      currentArrayKey = null;
    }
  }

  return obj;
}

function isMissing(fm, field) {
  return !(field in fm) || fm[field] === undefined || fm[field] === '';
}

function validate(fm, file) {
  const errors = [];
  const isTradeOff = file.includes('/trade-offs/') || file.includes('\\trade-offs\\');

  if (isTradeOff) {
    for (const field of TRADEOFF_REQUIRED_FIELDS) {
      if (isMissing(fm, field)) errors.push(`missing required field: ${field}`);
    }
    if (fm.related !== undefined && !Array.isArray(fm.related)) {
      errors.push(`related must be an array, got ${typeof fm.related}`);
    }
    if (Array.isArray(fm.related)) {
      for (const r of fm.related) {
        if (!/^\d+:\d+-[a-z0-9-]+$/.test(r)) {
          errors.push(`related entry "${r}" is not in the form "part:zero-padded-slug"`);
        }
      }
    }
    return errors;
  }

  for (const field of REQUIRED_FIELDS) {
    if (isMissing(fm, field)) errors.push(`missing required field: ${field}`);
  }

  if (fm.part !== undefined) {
    const partNum = Number(fm.part);
    if (!Number.isInteger(partNum) || partNum < 0 || partNum > 11) {
      errors.push(`part must be integer 0-11, got ${fm.part}`);
    }
  }

  if (fm.difficulty && !VALID_DIFFICULTY.includes(fm.difficulty)) {
    errors.push(`difficulty must be one of ${VALID_DIFFICULTY.join(', ')}, got ${fm.difficulty}`);
  }

  // Part 8 chapters must declare a theme so navigation and the Part 8 index
  // can group them without further heuristics.
  const isPart8 = file.includes('/part-8-case-studies/') || file.includes('\\part-8-case-studies\\');
  if (isPart8) {
    if (isMissing(fm, 'theme')) {
      errors.push('missing required field: theme (Part 8 chapters must declare a theme)');
    } else if (!VALID_CASE_STUDY_THEMES.includes(fm.theme)) {
      errors.push(`theme must be one of ${VALID_CASE_STUDY_THEMES.join(', ')}, got ${fm.theme}`);
    }
  } else if (fm.theme !== undefined) {
    errors.push('theme is only valid for Part 8 case-study chapters');
  }

  if (fm.module !== undefined && typeof fm.module !== 'string') {
    errors.push(
      `module must be a quoted string (got ${typeof fm.module} ${fm.module}). ` +
      `Use module: "X.Y" with quotes — unquoted "2.10" parses as float 2.1.`
    );
  }

  if (fm.module && !/^\d+\.\d+$/.test(fm.module)) {
    errors.push(`module must match X.Y format, got ${fm.module}`);
  }

  if (fm.module && fm.part !== undefined) {
    const modulePart = fm.module.split('.')[0];
    if (String(fm.part) !== modulePart) {
      errors.push(`module "${fm.module}" does not match part ${fm.part}`);
    }
  }

  if (fm.technologies !== undefined) {
    if (!Array.isArray(fm.technologies)) {
      errors.push(`technologies must be an array, got ${typeof fm.technologies}`);
    } else if (ALLOWED_TECHNOLOGIES) {
      for (const tech of fm.technologies) {
        if (!ALLOWED_TECHNOLOGIES.has(tech)) {
          errors.push(`technologies entry "${tech}" is not in scripts/technologies.json allowlist`);
        }
      }
    }
  }

  if (fm.tags !== undefined) {
    if (!Array.isArray(fm.tags)) {
      errors.push(`tags must be an array, got ${typeof fm.tags}`);
    } else {
      for (const tag of fm.tags) {
        if (!VALID_TAGS.has(tag)) {
          errors.push(`tags entry "${tag}" is not in the canonical list (see STYLE_GUIDE.md)`);
        }
      }
    }
  }

  // Prerequisite format "X.Y-slug" must resolve against MODULE_REGISTRY;
  // see STYLE_GUIDE.md "Prerequisite slugs".
  if (Array.isArray(fm.prerequisites)) {
    for (const p of fm.prerequisites) {
      if (!/^\d+\.\d+-[a-z0-9-]+$/.test(p)) {
        errors.push(`prerequisites entry "${p}" is not in the form "X.Y-slug"`);
      } else if (!MODULE_REGISTRY.has(p)) {
        errors.push(`prerequisites entry "${p}" does not resolve to any chapter`);
      }
    }
  }

  return errors;
}

async function checkFile(file) {
  fileCount++;
  const contents = await readFile(file, 'utf8');

  const frontmatterMatch = contents.match(/^---\n([\s\S]*?)\n---/);
  if (frontmatterMatch) {
    const unquotedModule = frontmatterMatch[1].match(/^module:\s+(\d+\.\d+)\s*$/m);
    if (unquotedModule) {
      errorCount++;
      console.error(`\u274c ${file}:`);
      console.error(
        `    module must be a quoted string: module: "${unquotedModule[1]}". ` +
        `Unquoted "${unquotedModule[1]}" parses as a float, breaking e.g. 2.10 -> 2.1.`
      );
      return;
    }
  }

  const fm = parseFrontmatter(contents, file);
  if (!fm) {
    errorCount++;
    return;
  }

  const errors = validate(fm, file);
  if (errors.length > 0) {
    errorCount++;
    console.error(`\u274c ${file}:`);
    for (const err of errors) console.error(`    ${err}`);
  }
}

async function main() {
  const files = [];
  for await (const f of glob('content/**/*.md')) files.push(f);

  if (files.length === 0) {
    console.log('No content files found.');
    exit(0);
  }

  // Pass 1: build the module registry so prereq validation has ground truth.
  for (const f of files) registerModule(f);

  // Pass 2: validate each file.
  await Promise.all(files.map(checkFile));

  if (errorCount > 0) {
    console.error(`\n\u274c ${errorCount} of ${fileCount} file(s) have frontmatter issues.\n`);
    exit(1);
  }

  console.log(`\u2713 All ${fileCount} files have valid frontmatter.`);
  exit(0);
}

main().catch((err) => {
  console.error('Unexpected error:', err);
  exit(2);
});
