---
lc_id: 3
title: "Longest Substring Without Repeating Characters"
slug: LC-003-longest-substring-without-repeating-characters
primary_chapter: part-3-pointers-window-prefix/03-sliding-window-variable
star: true
difficulty: medium
date_updated: 2026-05-25
languages: [python, java, cpp, go]
editorial_widget: e-LC003-longest-substring
---

# Longest Substring Without Repeating Characters

LC 3 is the canonical introduction to the variable-size sliding window. The signature problem in [Sliding window: variable size](../part-3-pointers-window-prefix/03-sliding-window-variable.md) is this one, and the lesson here is one sentence: when a window has to shrink to restore an invariant, you can either step the left pointer one character at a time, or you can keep a last-seen-index map and jump it in O(1). The shrink-loop teaches the pattern. The jump is the version to submit.

The diagnostic input is `"pwwkew"`. The answer is 3. The interesting beat is not that the optimum is `"wke"`. It's that the algorithm has to *forget* the leading `'w'` mid-stream, and that the second `'w'` later forces a second forget. Any candidate solution that treats duplicates as a stop condition rather than a window-shrink trigger fails on this input.

## The problem

Given a string `s`, return the length of the longest substring of `s` that contains no repeating characters. A substring is a contiguous slice; ties don't matter because the answer is an integer length, not the slice itself. Constraints are `0 <= s.length <= 5 * 10^4`, with `s` drawn from English letters, digits, symbols, and spaces (the printable-ASCII subset, 128 codepoints).[^1]

| Input | Expected | What it tests |
|---|---|---|
| `"abcabcbb"` | `3` | Three optima (`"abc"`, `"bca"`, `"cab"`); the canonical no-tricks case |
| `"bbbbb"` | `1` | Every step after the first jumps `l` one ahead; window stays length 1 |
| `"pwwkew"` | `3` | Two duplicate-jumps in six characters; the diagnostic |
| `"abba"` | `2` | The stale-entry trap; the bug detector |

That last row is what most "almost right" submissions die on. Hold it. Verbatim wording at [LC 3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

## Approach 1: brute force

Read the problem literally. Pick every starting index `i`, expand `j` from `i` while uniqueness holds, remember the longest run.

```python
# Brute force: O(n^2) — what we're replacing
def length_of_longest_substring_brute(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best
```

Each starting index walks until it hits a duplicate, so the worst case is roughly `n^2 / 2` character checks. At `n = 5 * 10^4` that's `~1.25 * 10^9` operations, past LeetCode's 1000-millisecond budget on the boss inputs.[^1] The code is correct on every sample, ships TLE on the hidden ones. Saying out loud *"this is O(n²); we can do better"* is the calibration line the next move needs.

## Approach 2: shrink-loop sliding window

The redundancy is visible the moment you watch brute force run. On `"pwwkew"` from `i = 0`, the inner loop scans `p, w, w` and bails. From `i = 1`, it scans `w, w` and bails. From `i = 2`, it scans `w, k, e, w` and bails. The inner loop *re-scans* characters every other start index already proved were duplicate-free.

One window, two pointers, one piece of state remembers what brute force forgets.

```python
# Shrink-loop: O(n) amortized, but per-step worst case is O(n)
def length_of_longest_substring_shrink(s):
    counts = {}
    l = 0
    best = 0
    for r, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while counts[ch] > 1:
            counts[s[l]] -= 1
            l += 1
        if r - l + 1 > best:
            best = r - l + 1
    return best
```

Outer `for` advances `r` once per character. Inner `while` shrinks `l` whenever the new character makes its count exceed one, and stops the moment it drops back. The amortized cost is `O(n)` by the textbook aggregate argument: each character enters the window once and leaves at most once, so total pointer movement is bounded by `2n`.[^2]

The trouble is the *per-step* cost. On a pathological input like a 50,000-character distinct prefix followed by a repeat of the first character, the inner loop drains the entire window character by character on a single advance of `r`. Amortized `O(n)`. Worst-case `O(n)` per step. The total still lands at `O(n)`, but the constant factor is roughly twice the optimum, and on truly adversarial sequences the LeetCode discussion thread for LC 3 documents shrink-loop submissions timing out where the jump version does not.[^3]

## Approach 3: last-index jump (optimal)

When the new character was last seen at index `prev`, the destination of `l` is knowable in `O(1)`: it's `prev + 1`. The shrink loop walks there one step at a time. Replace the `counts` map with a `last_index` map and the loop with a single assignment.

```python
def length_of_longest_substring(s):
    last = {}
    l = 0
    best = 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:    # guard is mandatory
            l = last[ch] + 1                # jump in O(1); no shrink loop
        last[ch] = r
        if r - l + 1 > best:
            best = r - l + 1
    return best
```

**Solution** — Python ([Java](./LC-003-longest-substring-without-repeating-characters/lc-3/sol.java) · [C++](./LC-003-longest-substring-without-repeating-characters/lc-3/sol.cpp) · [Go](./LC-003-longest-substring-without-repeating-characters/lc-3/sol.go))

```python
# LC 3. Longest Substring Without Repeating Characters
from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """LC 3: length of the longest substring of s with no repeating characters.

    One pass with a last-index map. For each character at position r, if it
    was seen at index `prev` AND `prev >= l` (i.e., the prior occurrence is
    inside the current window), jump l to prev + 1 in O(1) instead of
    shrinking step by step. The `prev >= l` guard is mandatory: stale
    entries from before the current window must be ignored, otherwise l
    can move backwards into discarded territory.
    O(n) time, O(min(n, sigma)) space; under ASCII sigma=128, space is O(1).
    """
    last_index: Dict[str, int] = {}
    l = 0
    best = 0
    for r, c in enumerate(s):
        if c in last_index and last_index[c] >= l:
            l = last_index[c] + 1
        last_index[c] = r
        if r - l + 1 > best:
            best = r - l + 1
    return best
```

> **Interactive widget:** [Longest Substring Without Repeating Characters (LC 3) — last-index jump](../widgets/e-LC003-longest-substring.yml) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: on `s = "pwwkew"`, the window expands to `"pw"` (best=2), the second `'w'` at `r=2` triggers a jump from `l=0` to `l=2`, the window grows to `"wke"` at `r=4` (best=3, the answer), and the second duplicate `'w'` at `r=5` triggers a second jump from `l=2` to `l=3`, ending on `"kew"` at length 3. Six iterations, two jumps, no inner loop.*

The widget animates exactly six outer iterations on `"pwwkew"`. Step 7 is the teaching beat: `last['p'] = 0` is now stale (its value sits below `l = 3`), and the guard would silently ignore it on a hypothetical later `'p'`. The shrink-loop form has no such hazard because it has no jump; the jump form trades one shrink loop for one guard, and the guard is the trade.

### Last-index jump: from O(2n) to O(n) amortized

The complexity bound on both Approach 2 and Approach 3 is amortized `O(n)`. What differs is the work per character. In Approach 2, every character enters the window via `r` and leaves the window via `l`; the amortized total is `2n` pointer moves, with the moves clustered (each duplicate triggers a streak of `l` advances). In Approach 3, every character is read exactly once by the outer loop, the inner work is at most one map read, one comparison, one assignment, and one map write. Total `n` outer iterations, `O(1)` inside each, no streaks. Wall-clock benchmarks on adversarial inputs show 1.5x to 3x speedups for the jump form over the shrink form.[^3]

The guard `last[ch] >= l` is the line that separates correctness from a silent wrong-answer bug. After processing `"pwwkew"` through index 5, `last['p'] = 0`. That entry is *stale*: `'p'` is no longer inside the window. If a later character were `'p'` again, the unconditional jump `l = last['p'] + 1 = 1` would slide `l` *backwards* into territory the algorithm already discarded. The guard says: only jump when the previous index lies inside the *current* window. Without it, the algorithm corrupts the window the moment any character recurs after a gap. With it, stale entries are silently overwritten on the next assignment.

The two equivalent formulations are an explicit `if last[ch] >= l: l = last[ch] + 1` (clearer) and an implicit `l = max(l, last.get(ch, -1) + 1)` (terser). Both are correct. Pick whichever the interviewer can read faster.[^4]

## Edge cases

**Empty string.** `""` returns `0`. The for-loop runs zero times; `best` stays at its initial 0. The C++ and Java idiomatic `s.size()` / `s.length()` return 0; the loop is skipped cleanly with no off-by-one.

**Single repeated character.** `"bbbbb"` returns `1`. Each iteration after the first finds `last['b']` inside the window, jumps `l` to `prev + 1` (i.e., to `r`), updates `last['b'] = r`, and records a window of length 1. The window never grows past one character; `best` never exceeds 1.

**Mixed case.** LC 3's character set treats `'a'` and `'A'` as distinct ASCII codepoints. `"AaAa"` returns `2`, not 1. The algorithm is character-set agnostic; the test harness exercises this.

## Common bugs

**Forgetting the `last[ch] >= l` guard.** The classic. On `"abba"`, after processing through `r = 2` (the second `'b'`), `l = 2`. At `r = 3` the algorithm reads `'a'` and finds `last['a'] = 0`. The unguarded jump sets `l = 1`, *backwards*. The window now spans `s[1..3] = "bba"`, which contains a duplicate `'b'`, and the reported answer is `1` instead of the correct `2`. The fix is the conditional `if last[ch] >= l` or the equivalent `max(l, ...)`.

**Off-by-one on window length.** Inclusive bounds `[l, r]` give length `r - l + 1`, not `r - l`. Submissions that drop the `+ 1` report every window length one short. On `"abcabcbb"`, the answer comes back as `2` instead of `3`.

**Updating `best` before fixing the window (shrink-loop form).** A submission that places `best = max(best, r - l + 1)` *before* the inner `while` records the still-invalid window's length and overshoots. The correct order is: extend, fix, record. The named-as-Pitfall-5 in algo.monster's pitfall list, with a worked example showing the wrong sequence.[^5]

**Using `if` instead of `while` (shrink-loop form).** A single-step `if` removes one character from the front of the window, but the duplicate may still be present. Most inputs survive because most duplicates need one step of shrink to fix; the bug surfaces on inputs like `"abba"` where the duplicate is several characters back. The jump form (Approach 3) sidesteps this entire bug class, which is one of the reasons it's the version to ship.[^5]

## Interview follow-ups

**How would you return the actual substring, not just its length?** Track `best_l` alongside `best_len`. Update both, but only update `best_l` on a strict-greater hit so the *first* longest substring wins ties; on a `>=` update, the *last* wins. Return `s[best_l : best_l + best_len]`.[^4]

**What if the constraint is "at most K distinct characters" instead of "no repeats"?** The K=1 instance is "no repeats", exactly LC 3 with `len(window) <= K` replacing the duplicate predicate. Generalise: keep a count map plus an integer `distinct` that increments when a key's count crosses `0 -> 1` and decrements when it crosses `1 -> 0`. Shrink while `distinct > K`. Same `O(n)`, same skeleton. The K=2 instance is [LC 904 — Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/); the parameterised LC 340 sits behind a paywall and is the chapter ladder's STRETCH placeholder.

**Can you avoid the hash map entirely for ASCII inputs?** When the alphabet is the LC 3 constraint set (printable ASCII, 128 codepoints), the hash map collapses to a fixed `int[128]` array initialised to -1. The C++ and Go reference implementations above already use this; in Java it's `int[] lastIndex = new int[128]; Arrays.fill(lastIndex, -1)`, and avoids the `HashMap<Character, Integer>` autoboxing on every put and get. Roughly 3x faster on benchmark inputs simply because hashing disappears.

**What if characters arrive one at a time?** The algorithm is already a single forward pass with `O(1)` work per character, so the offline and online versions are the same code. State is `(l, last_index, best)`; expose `next(c)` that updates all three and emits the running `best`. The unbounded-alphabet variant grows `last_index` to `O(n)`; under the LC 3 ASCII constraint, it caps at 128.

The bridge from this problem to its harder cousin is [LC 76 — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/), which keeps the variable-window scaffold but replaces the duplicate predicate with a cover-set predicate and an integer counter. Same loop shape, harder state.

## References

[^1]: doocs/leetcode, "LC 3 Longest Substring Without Repeating Characters." https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0003.Longest%20Substring%20Without%20Repeating%20Characters/README_EN.md

[^2]: Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*, 4th ed., MIT Press, 2022, Ch. 17 (aggregate analysis).

[^3]: LeetCode community discussion threads for LC 3 (login-gated; not mirrored).

[^4]: walkccc, "LeetCode 3." https://walkccc.me/LeetCode/problems/3/

[^5]: AlgoMonster, "3. Longest Substring Without Repeating Characters." https://algo.monster/liteproblems/3
