---
title: "How to use this handbook"
description: "How to read this handbook: who it's for, what to skip, how to pick a language, and the four questions every DSA resource ducks."
slug: 00-how-to-use
part: 0
chapter: 0
difficulty: beginner
prerequisites: []
date_updated: 2026-05-24
languages: [python, java, cpp, go]
ladder:
  core: []
  stretch: []
---

# How to use this handbook

Most readers reach this page after trying two or three other DSA resources and walking away without a plan. The Blind 75 gave you 75 problems and no through-line. NeetCode 150 grouped problems by category and told you to grind. Striver's A2Z sheet gave you 474 problems and watched a third of you quit by week six. None of them answered the four questions you actually showed up with: is this worth my time, where do I start, how will I know when I'm done, and which language do I write in.

This page answers those four. The next chapter starts where you stop reading.

## What you're looking at

The handbook is fifteen parts and roughly 120 chapters. Part 0, where you are now, covers the seven foundations every algorithmic chapter assumes: complexity notation, recursion, bit tricks, the math that actually shows up in interviews, and the language idioms that make Python, Java, C++, and Go read fluently. Parts 1 through 13 are the algorithms, organised by data-structure family and pattern: linear DS, search/sort, two pointers and sliding windows, stacks, linked lists, trees, recursion and backtracking, graphs, DP, greedy, bit manipulation, strings, and "design the data structure" problems. Part 14 is the interview process itself: pattern recognition, clarifying questions, communication, mock-interview drills, Amazon LP narration, and Meta's AI-assisted coding round.

Two companion surfaces sit alongside the parts. The Patterns Library is 37 short pages built around the question "when do I reach for X versus Y," read laterally after you've met the underlying algorithms. Appendix C ships fifty deep-dive editorials, one for every signature problem the chapters mark with a ★. Each editorial gets the full 4,000 to 6,000 word treatment: clarifying questions, three to five approaches walked from naive to optimal, edge cases, common bugs sourced from LeetCode Discuss, four-language reference solutions, and a step-trace.

Across the book, 92 hand-built interactive widgets animate the algorithms that prose alone can't carry. Forty-two of them are in chapter bodies; the other fifty are in the Appendix C editorials.

## The three reading paths

The handbook is sized for three explicit paths. Pick one before you start.

| Path | Problems | Time | Who it's for |
|---|---|---|---|
| **Recommended** | 160 (CORE problems on Progression Tracks) | ~107 hours / ~3 months | Default. The reader prepping for a FAANG-tier loop on a 12-week ramp. Bigger than NeetCode 150;[^1] far smaller than Striver A2Z.[^2] |
| **Core Mastery** | ~275 (every CORE in every algorithmic chapter) | ~5 months | The reader who wants chapter-mastery confirmation across all 15 parts. |
| **Comprehensive** | ~445 (CORE + STRETCH everywhere) + 50 editorials | ~7 to 8 months | Self-paced semester. Use the handbook the way you'd use a textbook. |

The numbers were calibrated against the obvious benchmarks. Blind 75[^3] is too small for breadth; NeetCode 150[^1] is the modern FAANG baseline; Striver A2Z[^2] is where self-study completion rates collapse. The Recommended path lands at 160 to keep deliberate practice tractable inside three months without falling off the cliff Striver-volume curricula see.[^4]

If you cannot tell which path is yours, pick Recommended. Path size is a forecast of effort, not a commitment. You can extend Recommended into Core Mastery later by working through the STRETCH ladder on chapters you didn't finish.

## How chapters work

Every algorithmic chapter ends with a **link-only LeetCode ladder** of three to five problems, split into two tiers.

CORE is three problems that span Easy, Medium, and Hard. Solving all three flips chapter mastery on. STRETCH is one or two optional extensions. Exactly one CORE problem per chapter wears a ★, the chapter's signature problem. The ★ also gets the chapter's worked-example treatment, the chapter's animated widget when one exists, and an Appendix C editorial.

Ladder entries are deliberately minimal: LC number, title, difficulty bracket, single pattern tag, link. No company tags (those live in per-company tracks at `content/dsa/per-company/`), no time estimates, no inline hints, no code. LeetCode owns the problem statements and runs the code; the handbook's value is the **sequencing and grouping**. The teaching lives in the chapter prose, the worked example, the flashcards, and the Appendix C editorial.

Roughly twenty-one chapters are foundation or framework material: Part 0 meta chapters, all of Part 14, a handful of others. They're exempt from the Easy/Medium/Hard span requirement and ship zero to two problems with no required spread. This page is one of them. There is no ladder here because you have not yet met any algorithms.

## How widgets work

About 45% of chapters carry an animated widget. The conventions are the same everywhere.

Every widget defaults to **paused at step zero**. Nothing autoplays. You step forward (Right), step back (Left), reset (R), or play and pause (Space). Each widget exposes a speed selector, a static-keyframe fallback for when JavaScript is off or `prefers-reduced-motion: reduce` is set, and an `aria-live` status line that announces the current step in plain English.[^5]

The visual language is fixed. Sorting and graph widgets use the eight-colour Wong palette,[^6] chosen so every state change is distinguishable across protanopia, deuteranopia, and tritanopia. Active states are orange. Visited cells are sky blue. Accepted answers are bluish green. Rejection is vermilion. There are no naked red/green pairs anywhere in the book to encode "good versus bad" or "visited versus unvisited," because roughly 8% of male readers and 0.5% of female readers experience red/green colour blindness.[^6]

Widget complexity is pinned by Bostock's 2014 three-level convention.[^7] Most chapters get a Level-0 hero image plus a Level-1 process widget. Level 2, full internal-state visibility, is reserved for the four hardest algorithms in the book: AVL rotations, Dijkstra, KMP's failure function, and segment trees with lazy propagation. The reasoning is Bostock's own: white-box visualisation has the greatest potential to explain and the highest burden on the reader. We pay that burden where the algorithm earns it and not before.

The default-paused stance is stricter than WCAG 2.2 SC 2.2.2 requires (which only kicks in at the five-second mark)[^8] and aligns with Mayer's segmenting principle: learner-paced beats system-paced for novices, with an effect size of d = 0.70.[^9]

## The four-language posture

Every code block in the book renders as a tabbed component with **Python, Java, C++, and Go** tabs. The choice is deliberate, not historical.

Python is the canonical text. When the prose says "the array `nums`," that name is in the Python tab. The Python tab's iteration model (`enumerate`, `zip`, `collections.Counter`, `heapq`) is the closest of the four to algorithmic-pseudocode style, and Python is LeetCode's default submission language.

Java exists because Java 21 is still the language of choice at most large engineering organisations for backend interviews: Amazon, Bloomberg, Stripe's JVM stack, parts of Google. The Java tab also surfaces boxing costs (`PriorityQueue<Integer>` autoboxes on every `offer` and `poll`) and overflow gotchas (`Integer.compare(a, b)` over `a - b`) that the higher-level languages hide.

C++ is required for systems and quant interviews. The baseline is C++17. Signed overflow is undefined behaviour. The compile is unforgiving. Both are pedagogically valuable.

Go is required because it has become the second most-common backend language at modern infrastructure-heavy companies (Stripe, Cloudflare, ByteDance). The Go tab also surfaces the slice-aliasing footgun on every chapter where a subarray view is taken, which is the most common chapter-code bug source across the book.

Same algorithm, possibly different data structure, is allowed and often necessary. An LRU cache is `OrderedDict` in Python, `LinkedHashMap` in Java, `list<pair> + unordered_map<key, iterator>` in C++, `container/list + map` in Go. All four are correct.

Pick one language for the interview. Read the others to deepen pattern recognition. [Choosing your interview language](./06-choosing-your-language.md) is the decision matrix; [Language idioms](./05-language-idioms.md) is the side-by-side reference you'll come back to.

## How to read

Three rules, in priority order.

**Do not skip Part 0.** Every algorithmic chapter cites it. Most readers want to skip it; most readers shouldn't. Skiena makes the same argument in *The Algorithm Design Manual*: the techniques half of the book exists because skipping fundamentals means re-deriving them on every problem.

**Read in part order, not topic order.** Parts 1 through 13 build on Part 0 and on each other. The Patterns Library is a lateral surface. Read it after a chapter, not before, because each pattern page is a "decision question" that only makes sense once you've met the underlying algorithms.

**Do the CORE problems before moving on.** Solving from scratch beats re-reading. The testing effect, the finding that retrieval practice produces stronger long-term retention than re-study even without feedback, has held up across forty years of educational psychology research and is the foundation under both the CORE-ladder design and the chapter flashcards.[^10]

## What this is not

It is not a competitive-programming book. Codeforces problems are different from interview problems and the techniques diverge after the first 50 hours. If you want CP, read Halim's *Competitive Programming Handbook*.

It is not a CS textbook. The proofs are not exhaustive. The exotic complexity classes (smoothed analysis, competitive ratios, the polynomial hierarchy) are out of scope. CLRS[^11] and Erickson are the right references for those.

It is not a cheatsheet. There is a Patterns Library that compresses pattern decisions, but the chapters themselves do the teaching. A reader who only skims will not finish a Medium under interview pressure.

It is a working handbook. You read a chapter, you solve its CORE three, you move on. The flashcards reload as spaced repetition. The widgets pause when you stop scrubbing. The book gets out of your way once you've decided to start.

[Computational complexity and Big-O](./01-complexity-big-o.md) is next. Read it tonight.

## References

[^1]: NeetCode 150 problem list, [neetcode.io/practice?tab=neetcode150](https://neetcode.io/practice?tab=neetcode150).

[^2]: takeuforward (Striver), "Strivers A2Z DSA Course/Sheet", [takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z).

[^3]: Yangshun Tay, "Blind 75" curated LeetCode list, originally posted on the Blind platform 2018, [techinterviewhandbook.org/grind75/](https://www.techinterviewhandbook.org/grind75/)

[^4]: Ericsson, K.A., Krampe, R.T., Tesch-Römer, C., "The Role of Deliberate Practice in the Acquisition of Expert Performance", *Psychological Review*, 100(3), 363-406, 1993, [eric.ed.gov/?id=EJ471947](https://eric.ed.gov/?id=EJ471947).

[^5]: W3C, "Understanding Success Criterion 2.2.2: Pause, Stop, Hide" (Level A), WCAG 2.2 Understanding Docs, [w3.org/WAI/WCAG22/Understanding/pause-stop-hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide).

[^6]: Wong, B., "Points of view: Color blindness", *Nature Methods*, 8, 441 (2011), DOI 10.1038/nmeth.1618, [nature.com/articles/nmeth.1618](https://www.nature.com/articles/nmeth.1618).

[^7]: Bostock, M., "Visualizing Algorithms" (June 26, 2014), [bost.ocks.org/mike/algorithms](https://bost.ocks.org/mike/algorithms/).

[^8]: MDN Web Docs, `prefers-reduced-motion`, [developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion).

[^9]: Mayer, R.E. and Pilegard, C., "Principles for Managing Essential Processing in Multimedia Learning", in Mayer (ed.) *The Cambridge Handbook of Multimedia Learning*, 2nd ed., Cambridge University Press, 2014.

[^10]: Roediger, H.L. and Karpicke, J.D., "Test-Enhanced Learning", *Psychological Science*, 17(3), 249-255, 2006, [pubmed.ncbi.nlm.nih.gov/16507066](https://pubmed.ncbi.nlm.nih.gov/16507066/).

[^11]: Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., *Introduction to Algorithms*, 4th ed., MIT Press, 2022, ISBN 978-0-262-04630-5.
