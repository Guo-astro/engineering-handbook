---
title: "Z-algorithm"
description: "Z-array as the prefix-match table on a string; the [l, r) window invariant that makes it linear; how it compares with KMP for exact pattern matching."
slug: 03-z-algorithm
part: 12
chapter: 3
difficulty: advanced
prerequisites:
  - part-12-strings-pattern-matching/02-kmp
  - part-1-linear-data-structures/02-strings
  - part-0-foundations/01-complexity-big-o
date_updated: 2026-05-25
languages: [python, java, cpp, go]
canonical_test: LC-1668
widgets: [w-40-z-array]
ladder:
  core: [LC-1668, LC-1163, LC-3008]
  stretch: [LC-3034, LC-214]
  star: LC-3008
---

# Z-algorithm

Gusfield published a 590-page book on string algorithms in 1997 and gave the Z-algorithm thirty pages, opening on §1.5 with a sentence that has aged well: *"Almost every string-matching problem we will study can be reduced to the question, for every position `i` in this string `s`, how long is the substring starting at `i` that matches a prefix of `s`?"* Answer that question for every `i` at once, in linear time, and exact pattern matching falls out as a corollary. Period detection falls out. Longest palindromic prefix falls out. Five interview problems on the LeetCode track collapse to "compute one Z-array and read it."

[KMP and the failure function](./02-kmp.md) answers a different question with the same time bound. Where KMP scans the text left to right and remembers how to skip after a mismatch, Z builds a table over the entire string and lets the caller read whichever entries the problem asks for. Two algorithms, both O(n + m), same asymptotic cost on identical inputs. The right choice between them is mostly stylistic, and the comparison table at the end of the chapter is the practical guide. What lives in the middle of the chapter is the single hardest construction in either: the `[l, r)` match window that makes Z linear.

## What the Z-array is

For a string `s` of length `n`, the Z-array `z[0..n-1]` is defined position by position. `z[i]` is the length of the longest substring starting at index `i` that is also a prefix of `s`. The 0th entry is special: by convention `z[0] = 0`, because the algorithm's recurrence starts at `i = 1` and never reads `z[0]`. Defining `z[0] = n` would special-case the math and confuse the loop.[^1]

Run that definition by hand on `s = "aabaabcaab"`, length 10.

```text
i:    0  1  2  3  4  5  6  7  8  9
s:    a  a  b  a  a  b  c  a  a  b
z:    0  1  0  3  1  0  0  3  1  0
```

Index 3 reads as: starting at position 3, the substring `"aab"` matches the prefix `"aab"` for 3 characters, then `s[3] = 'a'` versus `s[6] = 'c'` mismatches. Three matches; `z[3] = 3`. Index 4 reads as: starting at position 4, the single character `'a'` matches the prefix's first character, then `s[1] = 'a'` versus `s[5] = 'b'` mismatches. One match; `z[4] = 1`. Index 7 picks up `"aab"` again, this time running off the end of the string after three matches; `z[7] = 3`.

The pattern visible in those numbers is the algorithm's whole reason to exist. After computing `z[3] = 3`, the algorithm has *already* compared `s[3..5]` against `s[0..2]` and learned that the two are equal. Indices 4 and 5 sit inside the same matched span. Their Z-values can be read off from `z[1]` and `z[2]` without comparing characters at all. That is the saving the Z-algorithm cashes in. Watch the table: `z[4] = z[1] = 1`, `z[5] = z[2] = 0`. The same trick fires again after `z[7] = 3` is computed: `z[8] = z[1] = 1`, `z[9] = z[2] = 0`.

This is the central insight, and it has a name. The matched span the algorithm has most recently confirmed is called the **Z-box**, written as a half-open interval `[l, r)`. After `z[3] = 3`, the Z-box is `[3, 6)`. Inside that interval, every position `i` knows its Z-value for free, capped by where the box ends.

## The algorithm

Two state variables besides the array. `l` and `r` track the rightmost Z-box discovered so far. The invariant: `s[l:r]` equals `s[0:r-l]` and `r` is maximal among all such windows. Three branches in the main loop.

```python
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0                          # invariant: s[l:r] == s[0:r-l]
    for i in range(1, n):
        if i < r:                        # i is inside the current Z-box
            z[i] = min(r - i, z[i - l])  # mirror, capped at the box edge
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1                    # extend by direct comparison
        if i + z[i] > r:                 # the new match reaches further
            l, r = i, i + z[i]           # slide the window forward
    return z
```

The three branches read in order. When `i` lies outside the current box (`i >= r`), the algorithm starts fresh and extends by direct comparison from scratch. When `i` lies inside the box (`i < r`), the mirror at `k = i - l` is consulted. If `z[k]` is small enough to stay inside the box, the answer is `z[k]` and no character comparisons are needed. If `z[k]` is large enough that it would reach past `r`, the answer is at least `r - i` (the part of the mirror confirmed by the box) and possibly more, so the `while` loop extends from there. The `min(r - i, z[i - l])` cap encodes both subcases in one expression.

After every position, if the new match `[i, i + z[i])` extends past the previous `r`, the box slides to that new interval. The slide is the only place `r` ever advances, and `r` only ever advances forward.

### Why the inner loop is amortized linear

The `while` loop has no obvious bound. On any one iteration of the outer loop it could run anywhere from zero comparisons to `n` comparisons. Yet across the entire run, the total number of successful comparisons is bounded by `n`. The argument is one observation made twice.

Every successful character comparison inside the `while` strictly advances `r`. Look at the loop body: after each match, `z[i]` increases by one, and at the end of the outer iteration the slide condition `i + z[i] > r` triggers and sets `r` to `i + z[i]`. So one match means `r` grows by at least one. Across the whole run, `r` starts at 0 and can never exceed `n`, so it grows by at most `n` total. The total number of successful comparisons is therefore at most `n`.[^2]

Each outer iteration also performs at most one *failing* comparison after the trivial-init or mirror step, the one that stops the `while`. There are `n - 1` outer iterations, contributing at most `n - 1` failing comparisons. Sum: at most `2n - 1` character comparisons across the entire algorithm, which is O(n).[^1]

This is the same potential argument that bounds KMP's failure function in linear time: a counter that only moves one direction, summed over the run. The Z-algorithm and KMP share this proof shape because they share the underlying idea of inheriting work from prior matches; they differ in which counter is the protagonist and which direction it moves.

## Worked example: LC 1668

The cleanest place to watch the Z-algorithm earn its place is on a problem where the brute-force answer almost works. **LC 1668 (Maximum Repeating Substring)** asks: given strings `sequence` and `word`, return the largest `k` such that `word` repeated `k` times appears as a substring of `sequence`.[^3] On the sample input `sequence = "ababc"`, `word = "ab"`, the answer is 2 because `"abab"` is a substring; `"ababab"` is not.

The natural first attempt loops over every starting position in `sequence` and uses `String.contains` or its equivalent to check whether `word * k` appears. Correct, and within LC's time limits at the small constraint scale, but the asymptotic bound is `O(|sequence|² × |word|)` and the structure of the work is wasteful in exactly the way Z fixes: the same prefix-match check is performed thousands of times against the same indices.

The Z-algorithm replaces it with one preprocess plus one cheap scan. Build `s = word + "#" + sequence` with a sentinel that appears in neither input. Compute `z(s)`. Every position `i` in `s` past the sentinel where `z[i] >= |word|` is a position at which `word` occurs in `sequence`. To count repeats from a given start, walk forward in stride `|word|` and count consecutive matches. The longest run of consecutive `z[i] >= |word|` values at stride `|word|` gives the answer.

```python
from typing import List


def z_function(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def max_repeating(sequence: str, word: str) -> int:
    m = len(word)
    if m == 0 or m > len(sequence):
        return 0
    s = word + "#" + sequence
    z = z_function(s)
    best, n = 0, len(sequence)
    for start in range(n):
        i = m + 1 + start
        run = 0
        while i + m <= len(s) and z[i] >= m:
            run += 1
            i += m
        best = max(best, run)
    return best
```

**Solution** — Python ([Java](./03-z-algorithm/lc-1668/sol.java) · [C++](./03-z-algorithm/lc-1668/sol.cpp) · [Go](./03-z-algorithm/lc-1668/sol.go))

```python
# LC 1668. Maximum Repeating Substring
from typing import List


def z_function(s: str) -> List[int]:
    """Return the Z-array of s in O(n) time. z[0] = 0 by convention."""
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def max_repeating(sequence: str, word: str) -> int:
    """LC 1668: largest k such that word repeated k times is a substring of sequence."""
    m = len(word)
    if m == 0 or m > len(sequence):
        return 0
    s = word + "#" + sequence
    z = z_function(s)
    # Walk the Z-array over the text part, chaining matches at stride m.
    best = 0
    n = len(sequence)
    for start in range(n):
        i = m + 1 + start
        run = 0
        while i + m <= len(s) and z[i] >= m:
            run += 1
            i += m
        if run > best:
            best = run
    return best
```

The `+ "#" +` matters and is the most-skipped detail in beginner Z code. Without the sentinel, prefix matches in the text could spill across into suffix matches of the pattern, producing Z-values that mix the two boundaries. With the sentinel, no Z-value can reach past it; the pattern and the text are sealed from each other. Pick any character that appears in neither input. For LC's lowercase-letter constraints, `#` is universal.[^2]

> **Interactive widget:** [Z-array construction with the [l, r) match window](../widgets/w-40-z-array.yml) (panel `default`) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: on `s = "aabaabcaab"` the Z-algorithm runs through 19 steps. Window slides to `[3, 6)` after step 8 when `z[3] = 3` is computed, and again to `[7, 10)` after step 15. The first mirror reuse is step 9: `z[4] = z[1] = 1` is set with no character comparisons, because step 8's slide proved `s[3..5]` equals `s[0..2]`. Final array: `[0, 1, 0, 3, 1, 0, 0, 3, 1, 0]`. The two non-zero positions at index 3 and index 7 are the prefix `"aab"` reappearing.*

## What it actually costs

| Variant | Time | Space | Notes |
|---|---|---|---|
| Z-array construction | O(n) | O(n) | tight on adversarial inputs like `"aaaa..."` |
| Pattern matching `pattern + # + text` | O(n + m) | O(n + m) | equivalent to KMP's bound |
| Period detection from a built Z-array | O(n) extra zero | O(1) extra | one linear scan over an existing array |
| Naive substring search (the baseline) | O(n × m) | O(1) | times out at LC 3008's `n = 10^5`, `m = 10^5` |

The bound is *independent of alphabet size*. The only operation on characters is `==`, so the algorithm runs the same on ASCII, Unicode code points, or arbitrary objects with an equality predicate. KMP shares this property; Boyer-Moore does not, which is why Boyer-Moore tends to lose on small alphabets even when it wins on large ones.[^4]

The space bound is O(n) for the Z-array itself; the `[l, r)` state is two integers. There is no `O(n × m)` matrix anywhere — Z, like KMP, is a *streaming* algorithm dressed up as a table.

## When the pattern bends: three reductions worth knowing

Pattern matching is the canonical application, but the same primitive answers a few questions whose surface form looks unrelated.

**Period detection.** The smallest `i > 0` such that `i + z[i] == n` and `i` divides `n` is the period of `s`. If `s = "abcabcabc"`, then `z[3] = 6`, `3 + 6 = 9 = n`, and `3` divides `9`; the period is `3`.[^2] LC 459 (Repeated Substring Pattern) solves directly from this: the answer is "yes" iff such an `i` exists. The Z-array gives the period in O(n) extra zero work after construction.

**Longest palindromic prefix.** Build `s' = s + # + reverse(s)`, compute `z(s')`, find the largest `i` such that `z[i] + i == |s'|`. The match position in the second half corresponds to the longest prefix of `s` that equals its own reverse, that is, the longest palindromic prefix.[^5] LC 214 (Shortest Palindrome) reduces to this: prepend the reverse of everything past the longest palindromic prefix, and the result is the shortest palindrome containing `s` as a prefix.

**Pattern matching on integer arrays.** The Z-algorithm's logic depends only on equality between two elements, not on a string-specific operation. LC 3034 (Number of Subarrays That Match a Pattern I) converts an integer array into a `(+1, 0, -1)` direction-code array via pairwise comparisons, then runs Z over the codes to find every subarray matching the target sequence in O(n + m).[^6] The same code works on any sequence with a defined `==`.

The pattern across the three: if the question can be re-stated in the form *"where does the prefix re-appear inside this string?"*, Z fits. The reductions above re-state surprisingly different questions in that shape.

## Two pitfalls that bite

> [!WARNING]
> **Forgetting the cap on the mirror value.** Writing `z[i] = z[i - l]` instead of `z[i] = min(r - i, z[i - l])` lets the mirror copy a value that reaches past `r`, where the algorithm has not actually verified the match. The algorithm then claims `z[i]` matches characters at unverified positions and produces wrong answers on inputs like `"aaaabaa"` at `i = 6`.[^2] The cap is the load-bearing correctness step. Always write the `min`.

> [!WARNING]
> **Off-by-one between half-open `[l, r)` and closed `[L, R]`.** The original Codeforces tutorial mixes both conventions: closed-interval prose, half-open code with an `R--` at the end of each branch.[^7] Implementations that copy the prose into a half-open codebase fail with `i <= r` instead of `i < r`, which makes the mirror branch fire on the boundary where the mirror value is undefined. Pick one convention. The cp-algorithms.com half-open convention used above tests `i < r` and slides with `r = i + z[i]`. Match it everywhere — pseudocode, all four language samples, and any narration of the algorithm. Mixing produces a silent off-by-one that costs an interview.

A third pitfall worth naming briefly: defining `z[0] = n` because the whole string trivially matches itself. The recurrence reads `z[i - l]` when `i < r`; if `i - l` happens to equal 0, the read returns `z[0]`. Setting `z[0] = n` corrupts the mirror initialization. Set `z[0] = 0`; the algorithm never reads it for any other purpose.

## KMP versus Z: when to pick each

KMP and Z compute different but mutually convertible values in the same time bound.[^8] On a pure pattern-match problem (LC 28, LC 459), an interviewer who asks "linear-time string match" accepts either, and most LC editorials show both. The choice is mostly about which *table* the problem naturally asks for.

| Concern | KMP (chapter 12.2) | Z-algorithm (this chapter) |
|---|---|---|
| Pattern-matching time | O(n + m) | O(n + m) |
| Space | O(m) for the failure function over the pattern | O(n + m) for Z over `pattern + # + text` |
| What it naturally answers | "scan the text once and skip after mismatches" | "for every position, how long is the prefix-match here?" |
| Streaming over an unknown-length text | direct (the failure function is built once over the pattern) | requires the full text up front (Z is built over a concatenation) |
| Period detection | direct (failure function exposes periods) | direct (Z-value plus index) |
| Longest palindromic prefix | possible via reversal trick | natural via `z(s + # + reverse(s))` |
| Pattern matching on arbitrary objects with `==` | works | works |
| Mental model | a state machine that scans | a table that the caller reads |
| Whiteboard from memory | most readers can sketch the failure function | many readers slip on the `[l, r)` cap |
| Historical dominance | textbook standard since 1977 | competitive-programming standard since the early 2000s |

The asymmetry to remember: **KMP scales over streams, Z scales over tables.** When the problem is "find this pattern in this text once" and the text arrives one character at a time, KMP fits naturally. When the problem is "tell me everything about how the prefix of this string interacts with the rest of it", whether that means period, palindromic prefix, or all match positions, Z fits naturally because the prefix-match table is exactly what you wanted.

LC 3008 is the chapter's signature problem and a clean illustration. The task is to find, for two patterns `a` and `b` and a text `s`, every index where `a` occurs in `s` such that `b` also occurs within distance `k`. The solution computes `z(a + # + s)` and `z(b + # + s)`, extracts two sorted index lists, and sweeps with a two-pointer or binary search for the distance constraint. KMP would solve it too, by running the failure-function scan twice; the cost is identical. The reason editorial implementations reach for Z is that the problem's natural ask, "every match position", *is* a table, and Z is the table.

The honest closing on the comparison: pick KMP first when teaching yourself string matching, pick Z first when the problem asks for the prefix-match table directly. Carry both. The two algorithms are not rivals; they are the same problem viewed through different lenses, and the lens that fits the question is the one to reach for.

## Problem ladder

### CORE (solve all three to claim chapter mastery)

- [LC 1668 — Maximum Repeating Substring](https://leetcode.com/problems/maximum-repeating-substring/) [Easy] • z-algorithm
- [LC 1163 — Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/) [Hard] • z-algorithm *(reference: Python only)*
- [LC 3008 — Find Beautiful Indices in the Given Array II](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/) [Hard] • z-algorithm ★ *(reference: Python only)*

### STRETCH (optional)

- [LC 3034 — Number of Subarrays That Match a Pattern I](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/) [Medium] • z-algorithm *(reference: Python only)*
- [LC 214 — Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) [Hard] • z-algorithm *(reference: Python only)*

LC 28 (Find the Index of the First Occurrence in a String) is the canonical "linear-time substring search" problem and intentionally absent from this ladder. Chapter 12.0 owns it as CORE; the framing, Z replaces KMP for an O(n + m) solution via `z(pattern + # + text)`, is a corollary of the worked example above. LC 459 (Repeated Substring Pattern) is owned by [KMP and the failure function](./02-kmp.md) and admits a Z solution from the period reduction.

LC 3034 sits in STRETCH as the M slot for the chapter's E/M/H span; the algorithm transfer (characters to integer codes) is the lesson. LC 214 is the reverse-and-concatenate trick rewarded in the editorial; its inclusion reinforces that the same primitive answers questions about palindromes that look unrelated to string matching at first glance.

## Where this leads

The Z-array and KMP's failure function are the two foundational linear-time string-matching primitives, and both extend naturally to richer problems. [Tries for multi-pattern matching (Aho-Corasick intuition)](./04-aho-corasick.md) takes the failure-link idea from KMP and bolts it onto a trie, lifting linear-time matching from one pattern to many. [Suffix array](./05-suffix-array.md) generalises further: rather than answering "where does *this* prefix appear?", the suffix array answers "where does *any* substring of `s` appear?" in O(n log n) construction, and several constructions (Karkkainen-Sanders, DC3) use Z-array-style amortization arguments as building blocks.

The other branch leads sideways. [Rabin-Karp](./01-rabin-karp.md) is the third linear-time string-matching algorithm, with a different trade-off profile: O(n + m) expected time but O(n × m) worst case, plus the practical advantage of generalising to multiple patterns and 2D matching with one rolling hash. The chapter's pattern decision page lays out KMP versus Z versus Rabin-Karp side by side; this chapter is the middle entry of that triple.

## References

[^1]: Dan Gusfield, *Algorithms on Strings, Trees, and Sequences: Computer Science and Computational Biology*, Cambridge University Press, 1997.

[^2]: cp-algorithms.com, "Z-function and its calculation." <https://cp-algorithms.com/string/z-function.html>.

[^3]: walkccc.me, "1668. Maximum Repeating Substring." <https://walkccc.me/LeetCode/problems/1668/>.

[^4]: Jeff Erickson, *Algorithms* (online textbook), Chapter 6 §6.2 "String Matching." Treats prefix-function methods (KMP, Z) under the same amortized-window argument and notes the alphabet-independence property that distinguishes both from Boyer-Moore. <https://jeffe.cs.illinois.edu/teaching/algorithms/>.

[^5]: leetcodethehardway.com, "0214 - Shortest Palindrome (Hard)." <https://leetcodethehardway.com/solutions/0200-0299/shortest-palindrome-hard>.

[^6]: walkccc.me, "3034. Number of Subarrays That Match a Pattern I." <https://walkccc.me/LeetCode/problems/3034/>.

[^7]: paladin8, "Z Algorithm." Codeforces blog entry 3107, 2010. <https://codeforces.com/blog/entry/3107>.

[^8]: cp-algorithms.com, "Prefix function — Knuth-Morris-Pratt." <https://cp-algorithms.com/string/prefix-function.html>.
