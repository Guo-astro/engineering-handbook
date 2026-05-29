#!/usr/bin/env python3
"""One-shot migration: rewrite [code-tabs ...] and [widget ...] shortcodes
in DSA chapters into GitHub-renderable Markdown.

[code-tabs slug="<chapter>/<problem>" langs="python,java,cpp,go"]
  -> **Solution** -- Python ([Java](./<chapter>/<problem>/sol.java) ...
     ```python
     <contents of ./<chapter>/<problem>/sol.py>
     ```

[widget id="<id>" panel="<panel>"]
  -> > **Interactive widget:** [<title>](../widgets/<id>.yml) -- panel <panel>

Run from the hld-handbook repo root, then archive this script.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DSA = REPO / "content" / "dsa"
WIDGETS = DSA / "widgets"

CODE_TABS_RE = re.compile(r'\[code-tabs slug="([^"]+)" langs="([^"]+)"\]')
WIDGET_RE = re.compile(r'\[widget id="([^"]+)"(?: panel="([^"]+)")?\]')

LANG_LABEL = {"python": "Python", "java": "Java", "cpp": "C++", "go": "Go"}
LANG_EXT = {"python": "py", "java": "java", "cpp": "cpp", "go": "go"}

errors: list[str] = []


def widget_title(widget_id: str) -> str:
    """Extract `title:` from the widget YAML spec; fall back to the id."""
    spec = WIDGETS / f"{widget_id}.yml"
    if not spec.exists():
        errors.append(f"missing widget spec: {spec}")
        return widget_id
    for line in spec.read_text().splitlines():
        m = re.match(r'^title:\s*"?([^"\n]+?)"?\s*$', line)
        if m:
            return m.group(1).strip()
    return widget_id


def replace_code_tabs(md_path: Path, slug: str, langs: list[str]) -> str:
    """Build the inline-Python + sibling-language replacement block."""
    base_dir = md_path.parent
    code_dir = base_dir / slug
    if "python" not in langs:
        errors.append(f"{md_path}: code-tabs slug={slug} has no python langs")
        return f"[code-tabs slug=\"{slug}\" langs=\"{','.join(langs)}\"]"

    py_file = code_dir / "sol.py"
    if not py_file.exists():
        errors.append(f"{md_path}: missing {py_file}")
        return f"[code-tabs slug=\"{slug}\" langs=\"{','.join(langs)}\"]"

    py_source = py_file.read_text().rstrip("\n")

    others = [l for l in langs if l != "python"]
    if not others:
        return f"```python\n{py_source}\n```"

    link_parts = []
    for lang in others:
        target = code_dir / f"sol.{LANG_EXT[lang]}"
        if not target.exists():
            errors.append(f"{md_path}: missing {target}")
            continue
        rel = f"./{slug}/sol.{LANG_EXT[lang]}"
        link_parts.append(f"[{LANG_LABEL[lang]}]({rel})")

    if link_parts:
        header = f"**Solution** — Python ({' · '.join(link_parts)})"
    else:
        header = "**Solution** — Python"

    return f"{header}\n\n```python\n{py_source}\n```"


def replace_widget(widget_id: str, panel: str | None) -> str:
    title = widget_title(widget_id)
    rel = f"../widgets/{widget_id}.yml"
    suffix = f" — panel: `{panel}`" if panel else ""
    return (
        f"> **Interactive widget:** [{title}]({rel}) — "
        f"rendered on the website; the YAML spec describes the keyframes.{suffix}"
    )


def rewrite_one(md_path: Path) -> tuple[int, int]:
    text = md_path.read_text()
    code_tabs_n = 0
    widget_n = 0

    def code_tabs_sub(m: re.Match[str]) -> str:
        nonlocal code_tabs_n
        code_tabs_n += 1
        slug = m.group(1)
        langs = [l.strip() for l in m.group(2).split(",") if l.strip()]
        return replace_code_tabs(md_path, slug, langs)

    def widget_sub(m: re.Match[str]) -> str:
        nonlocal widget_n
        widget_n += 1
        return replace_widget(m.group(1), m.group(2))

    new_text = CODE_TABS_RE.sub(code_tabs_sub, text)
    new_text = WIDGET_RE.sub(widget_sub, new_text)

    if new_text != text:
        md_path.write_text(new_text)
    return code_tabs_n, widget_n


def main() -> int:
    if not DSA.is_dir():
        print(f"DSA dir missing: {DSA}", file=sys.stderr)
        return 2

    md_files = sorted(DSA.rglob("*.md"))
    total_ct = total_w = touched = 0
    for md in md_files:
        ct, w = rewrite_one(md)
        if ct or w:
            touched += 1
        total_ct += ct
        total_w += w

    print(f"Files touched: {touched} / {len(md_files)}")
    print(f"[code-tabs] rewrites: {total_ct}")
    print(f"[widget]    rewrites: {total_w}")

    if errors:
        print(f"\n{len(errors)} issue(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
