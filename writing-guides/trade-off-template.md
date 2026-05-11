# Trade-off Chapter Template

**Canonical template for all trade-offs chapters.** Decision-comparison pages that give the reader a defensible mental model for choosing between two (or more) competing approaches. Every trade-offs chapter MUST follow this structure exactly.

**Target audience:** Engineers preparing for Staff+ system design interviews + practicing engineers making real production decisions.

---

## Hard constraints

| Constraint | Value |
|---|---|
| H2 count | **exactly 13** (outside code fences) |
| Total words | **1,800-2,800** (dense, opinionated, decision-focused) |
| Mermaid diagrams | **minimum 3** with italic captions (decision flowchart required) |
| Footnotes | **10-18** `[^N]` markers, every one with matching `[^N]:` definition |
| Frontmatter status | `complete` |
| Anti-patterns banned | `You covered/learned/saw X in [Chapter]`, `Part N Chapter M`, `Chapter N.M` |
| Cross-references | Full chapter title as link text with relative path |

---

## Exact document structure

```
---
title: "[Option A] vs [Option B]"
description: "One-sentence decision guide, < 160 chars."
section: trade-offs
difficulty: intermediate
prerequisites:
  - (2-4 slugs from teaching chapters that cover the underlying concepts)
tags: [tag1, tag2, ...]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: complete
---

# [Option A] vs [Option B]

> **TL;DR.** One-paragraph summary: the core tension, the default recommendation, and the key condition that flips the choice. 60-100 words. Must name the specific dimension that decides (latency, consistency, operational complexity, etc.).

## Learning Objectives

3-4 bullets. Each starts with an action verb (Compare, Identify, Justify, Evaluate). Each is a concrete, checkable outcome.

- Compare X and Y across [specific dimensions].
- Identify the workload characteristics that favor X over Y.
- Justify a hybrid approach that combines X and Y for [specific scenario].
- Evaluate real-world systems that made this choice and explain why.

**Word budget: 60-100 words.**

## The Core Trade-off

Why this choice matters. What you gain and lose on each side. The fundamental tension expressed in concrete engineering terms, not abstract platitudes. Name the specific metric that moves in opposite directions (e.g., "write latency rises as consistency strengthens"). 200-350 words.

One Mermaid diagram: a conceptual comparison (architecture overview, data flow contrast, or spectrum diagram).

**Word budget: 200-350 words.**

## Side-by-Side Comparison

Detailed comparison table with 6-8 dimensions.

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Latency | ... | ... |
| Consistency | ... | ... |
| Complexity | ... | ... |
| Cost | ... | ... |
| Scale ceiling | ... | ... |
| Failure mode | ... | ... |

Follow with 2-3 paragraphs analyzing the non-obvious rows: where does the table mislead, what dimension dominates in practice, what the table cannot capture.

**Word budget: 250-400 words.**

## When to Pick [Option A]

3-5 concrete scenarios with justification. Each scenario names a workload type, a scale range, and a specific product/company where applicable. Real numbers. 200-350 words.

**Word budget: 200-350 words.**

## When to Pick [Option B]

Same structure. 200-350 words.

**Word budget: 200-350 words.**

## The Hybrid Path

Most production systems live in the middle. How to combine or layer the two approaches. Real examples of companies doing this (named systems, concrete numbers). This section should be the one the reader bookmarks. 200-350 words.

One Mermaid diagram: architecture or decision flow showing the hybrid approach.

**Word budget: 200-350 words.**

## Real-World Examples

2-3 companies and their specific choices. Name the internal system, the scale, the year, and the outcome. Prefer primary sources (engineering blogs, papers, conference talks). 200-400 words.

**Word budget: 200-400 words.**

## Common Mistakes

3-5 `> [!WARNING]` callout blocks. Each names a specific mistake, why engineers make it, and what to do instead. 150-250 words.

> [!WARNING]
> **[Mistake headline].** Why it happens and what to do instead. 2-3 sentences.

**Word budget: 150-250 words.**

## Decision Checklist

5-7 checkbox items. Each is a specific question the reader evaluates for their system. Not generic; tied to the specific trade-off dimensions discussed above.

- [ ] Specific evaluative question about the reader's workload?
- [ ] ...

**Word budget: 80-120 words.**

## Key Takeaways

4-5 bullets. Defensible, memorable positions the reader can cite in an interview. Not a recap; a distilled insight.

**Word budget: 100-150 words.**

## Further Reading

4-6 curated external links with one-sentence annotations. Engineering blogs, papers, conference talks.

**Word budget: 100-150 words.**

## Flashcards

6-8 question/answer pairs using `<details>`/`<summary>`.

<details>
<summary><strong>Q: When does [Option A] outperform [Option B]?</strong></summary>

A: Specific answer in 2-3 sentences tied to concrete metrics.

</details>

**Word budget: 200-300 words.**

## References

Footnote definitions. Every `[^N]` marker in the body must have a matching `[^N]:` definition here. 10-18 references typical.

[^1]: Author or Org. "Title". Publication/Year. URL.
[^2]: ...

Order by N ascending. Prefer primary sources.

**Word budget: not counted toward prose budget.**
```

---

## Total word budget reconciliation

| Section | Budget |
|---------|-------:|
| TL;DR | 80 |
| Learning Objectives | 80 |
| The Core Trade-off | 275 |
| Side-by-Side Comparison | 325 |
| When to Pick A | 275 |
| When to Pick B | 275 |
| The Hybrid Path | 275 |
| Real-World Examples | 300 |
| Common Mistakes | 200 |
| Decision Checklist | 100 |
| Key Takeaways | 125 |
| Further Reading | 125 |
| Flashcards | 250 |
| **Total** | **~2,685** |

Aim for **1,800-2,800 words total**. If exceeding 2,800, tighten Side-by-Side Comparison prose and Real-World Examples first. If below 1,800, expand The Core Trade-off and The Hybrid Path.

---

## Voice and style

- **Opinionated and decision-focused.** Every section drives toward "here is what you should pick and why."
- **No marketing voice.** No "amazing", "powerful", "cutting-edge", "seamless", "robust".
- **No encyclopedia voice.** No "X is a technique that..."
- **Name real things.** Products (DynamoDB, CockroachDB, Kafka), techniques (quorum reads, write-ahead log), numbers (100K QPS, 5ms p50).
- **Dense.** These are reference pages. Every sentence earns its place.

---

## Diagram guidelines

- Minimum 3 Mermaid diagrams.
  - **Required:** Decision flowchart (`graph TD` or `flowchart TD`) showing the branching logic.
  - **Required:** Comparison architecture or data flow showing both approaches side by side.
  - **Third:** Author's choice, state diagram, sequence diagram, or hybrid architecture.
- Every diagram has a one-line italic caption immediately below the closing fence.
- No ASCII box diagrams. No external image links.

---

## Validation checklist (writer runs before returning)

- [ ] H2 count is exactly 13 outside code fences
- [ ] Word count is 1,800-2,800
- [ ] Minimum 3 Mermaid diagrams, each with italic caption
- [ ] 10-18 `[^N]` footnotes, every marker has matching definition
- [ ] Frontmatter has `status: complete`
- [ ] No "You covered/learned/saw X in [Chapter]" phrasing
- [ ] No "Part N Chapter M" or "Chapter N.M" references
- [ ] Cross-refs use full chapter title as link text with relative path
- [ ] Decision flowchart diagram is present
