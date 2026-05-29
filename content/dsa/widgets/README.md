# Widget specs — `content/dsa/widgets/`

One file per widget. Each file is the **authoritative source** for a single widget's
runtime spec: type, level, modes, caps, commands, per-panel canonical input, keyframe
trace, and the static-fallback image path.

The chapter Markdown frontmatter only references widgets by id (e.g. `widgets:
[w-09-sliding-window-expansion]`). Everything else lives here.

## Why this layout

Three reasons.

**One: chapter frontmatter stays human-sized.** Authors edit ~14 lines of frontmatter,
not ~200. The widget spec is too long to inline in a chapter and too detailed to
duplicate across the two-or-three chapters that share a panel.

**Two: shared widgets get one source of truth.** A panel-selector widget like
`w-31-dp-table-fill` mounts on four chapters; if the spec lived in chapter
frontmatter, four chapters would have to stay in sync.

**Three: the build can validate keyframe traces before the chapter ships.** CI's
`make check:widget-spec` parses every file in this directory, asserts each panel has
≥ 4 keyframes, and refuses to build a chapter that references a widget id with no
file here.

## File naming

`<widget-id>.yml` — the same id used in:

- `_widget-registry.yml` (the thin index; "which chapters use this widget")
- chapter frontmatter `widgets: [...]` lists
- `widget-specs.md` (the design notes; this folder ships the runtime spec — `widget-specs.md`
  ships the design rationale)

## Schema

```yaml
id: <widget-id>                             # must equal the filename stem
title: "<Human-readable widget title>"
type: <single-panel | dual-panel-shared | three-way-shared | four-way-shared
       | editorial-single-panel>
level: <0 | 1 | 2>                          # Bostock — see widget-architecture.md §6
modes: [preset, randomize, edit]            # subset; preset is mandatory

# Hard input bounds. Form refuses inputs past the cap with the §6.3 message.
caps:
  array_length: { min: 4, max: 32 }
  values: { min: -99, max: 99 }
  # Free-form per widget; see widget-specs.md for the per-widget caps table.

# Widget-specific commands beyond AlgoStep's default vocabulary
# (compare / swap / setVar / etc, documented in widget-architecture.md §2.4).
commands:
  - name: <commandName>
    payload: { <field>: <type> }
    description: "<what the renderer does>"

# Static fallback rendered at build time (for prefers-reduced-motion + no-JS).
static_fallback:
  generator: jsdom                          # default; some widgets use a hand-baked SVG
  output: site/static/widgets/<widget-id>-fallback.svg
  keyframes_used: [0, n_steps/4, n_steps/2, n_steps-1]   # which steps to capture

# One block per panel. Single-panel widgets list `default` only.
panels:
  <panel-key>:
    chapter: <chapter-id>                   # e.g. "3.2"
    label: "<selector label shown in panel switcher>"
    canonical_input: |
      <YAML literal block — the exact preset input for this panel>
    presets:
      - id: <preset-id>
        label: "<dropdown label>"
        input: <input value or block>
    n_steps: <integer>                      # length of the step buffer
    keyframes:                              # the depth — full step trace
      - step: 0
        kind: init
        state: { <free-form per widget> }
        narration: "<aria-live string for this step>"
      - step: 1
        kind: <commandName>                 # one of the commands above
        payload: { ... }
        state: { ... }
        narration: "..."
      # ... every step the renderer consumes ...

selector_default: <panel-key>               # multi-panel only: which panel renders first

notes: |                                    # optional free-form
  <design notes, citations, links to widget-specs.md §N>
```

## What lives WHERE

| Concern | File |
|---|---|
| Which chapters use a widget | `_widget-registry.yml` (thin index) |
| Widget design rationale (why Level 2, why preset-only, etc.) | `widget-specs.md` |
| Widget runtime spec (panels, presets, keyframes, narration) | **this directory** |
| Renderer JS code | `site/static/js/widgets/<widget-id>/` |
| Static fallback SVG | `site/static/widgets/<widget-id>-fallback.svg` (generated) |
| Chapter that mounts the widget | `widgets: [<widget-id>]` in chapter frontmatter |

## On-demand creation

Most of the 92 widgets do not have a file here yet. They get one when the chapter
that mounts them is being authored. The `@dsa-write` agent's contract:

1. Reads `widget-specs.md §N` for the widget's design notes.
2. Reads the chapter's research doc for the worked example's exact keyframe trace.
3. Writes `content/dsa/widgets/<widget-id>.yml` with the full spec above.
4. Updates `_widget-registry.yml` to point its entry at the new file.
5. The chapter frontmatter only ever lists the id.

If a widget is shared (panel-selector type), the *first* chapter to mount it creates
the file with the first panel's spec; subsequent chapters add panels via PR.

## Phase 1 exemplars

Four files are scaffolded for Phase 1 (Part 3 vertical slice):

- `w-08-two-pointers-3sum.yml` — single-panel chapter widget
- `w-09-sliding-window-expansion.yml` — dual-panel-shared
- `w-10-prefix-sum-cumulative.yml` — single-panel chapter widget
- `w-35-prefix-sum-hash-combo.yml` — single-panel chapter widget (reuses #10's array row)

And one editorial exemplar:

- `e-LC001-two-sum.yml` — editorial-single-panel (animates the optimal solution to LC 1)

These five files are the reference shape. Every subsequent widget yml mirrors one of them.
