---
lc_id: 5
title: "Longest Palindromic Substring"
slug: LC-005-longest-palindromic-substring
primary_chapter: part-9-dynamic-programming/10-palindrome-dp
star: true
difficulty: medium
date_updated: 2026-05-25
languages: [python, java, cpp, go]
editorial_widget: e-LC005-longest-palindrome
---

# Longest Palindromic Substring

LC 5 is the cleanest illustration of why two algorithms with identical Big-O can ship to wildly different production fates. The 2D DP table and expand-around-centers are both O(n²); only one of them allocates a million booleans on the way. At LC 5's stated `n <= 1000` ceiling[^1], the brute-force O(n³) approach hits ~10⁹ operations and times out; the two O(n²) approaches hit ~10⁶ and finish in well under a millisecond. The choice between the two `O(n²)`s is what the chapter is about.

The lesson is one sentence. Every palindrome has a center — either one character (odd length) or the gap between two adjacent characters (even length) — so iterating over the `2n - 1` candidate centers and pushing outward at each is sufficient. No table, no allocation, no by-length fill order to remember.

## The problem

Given a string `s`, return any longest contiguous substring of `s` that reads the same forward as backward. Constraints: `1 <= s.length <= 1000`, alphabet limited to digits and English letters. If multiple maximum-length palindromes exist, the judge accepts any of them.[^1]

| Input | Expected | What it tests |
|---|---|---|
| `"babad"` | `"bab"` or `"aba"` | Multi-valid-answer policy; tie at length 3 |
| `"cbbd"` | `"bb"` | Even-length palindrome; misses on odd-only implementations |
| `"a"` | `"a"` | Length-1 base case |
| `"racecar"` | `"racecar"` | Already-palindrome; the full string wins |

LC 5 wants the substring itself, not its length. It is a small detail that costs candidates an obvious extra five minutes when they only tracked `max_len`. Verbatim wording at [LC 5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/).

## Approach 1: brute force

Translate the statement directly. Enumerate every `(i, j)` with `i <= j`, check the substring for palindromicity in O(j - i), and track the longest hit.

```python
# Brute force: O(n^3) — what we're replacing
def longest_palindrome_brute(s: str) -> str:
    n = len(s)
    best_l, best_r = 0, 0

    def is_palin(lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    for i in range(n):
        for j in range(i, n):
            if (j - i) > (best_r - best_l) and is_palin(i, j):
                best_l, best_r = i, j
    return s[best_l:best_r + 1]
```

The work that's wasted is visible on the second-to-last line: `is_palin(i, j)` checks `s[i] == s[j]`, then runs the entire palindromicity check on `s[i+1..j-1]` from scratch. That inner range is also a substring whose palindromicity the algorithm computes again at a different `(i, j)`. Time `O(n³)`, space `O(1)`. At `n = 1000` that's roughly `5 × 10⁸` comparisons in the worst case, which TLEs on LeetCode's ~1-second budget for Python and Java.[^2]

The fix is to stop recomputing `is_palin(i+1, j-1)`. Either materialize it in a table and read it once, or fold the palindromicity check into the iteration so that the work is reused implicitly. Both fixes get to O(n²); they differ on space and on what the iteration looks like.

## Approach 2: the 2D DP table

Define `is_palin[i][j] = True` iff `s[i..j]` is a palindrome. The recurrence reads:

```text
is_palin[i][j] = (s[i] == s[j]) AND (j - i < 2 OR is_palin[i+1][j-1])
```

Length-1 cells are trivially `True`; length-2 cells are `True` iff the two characters match. For length `L >= 3`, the cell depends on the strictly inner range of length `L - 2`, which is the row *below* and the column to the *left*.[^3]

Critically, the fill order is by length, not by row. The cell `is_palin[i][j]` reads `is_palin[i+1][j-1]`. Filling top-to-bottom (`for i in 0..n: for j in i..n`) reads cells that have not been computed yet; the bug surfaces as a correct length-1/length-2 diagonal followed by every length-3+ palindrome reported as missing. The correct outer loop iterates over length `L = 1, 2, 3, ..., n`, then over the start index `i`, with `j = i + L - 1`. By the time you compute the length-L cell, every length-(L-2) cell already has its value.

Time `O(n²)`, space `O(n²)`. At `n = 1000` that's `~10⁶` operations and `~10⁶` booleans (~1 MB). It passes. The table version is also the natural primer for LC 647 (count palindromic substrings, same predicate) and LC 132 (min cuts, layers a 1D DP on top). The next approach has the same asymptotic time and zero allocation.

## Approach 3: expand around centers (optimal)

Every palindrome has a center. For odd-length palindromes the center is a single character; for even-length palindromes the center is the gap between two adjacent characters. There are exactly `2n - 1` candidate centers (`n` character-centers plus `n - 1` between-character centers). For each candidate, push two pointers outward as long as `s[left] == s[right]`. The longest expansion seen across all centers is the answer.[^4][^2]

```python
def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    best_l, best_r = 0, 0
    for i in range(len(s)):
        l1, r1 = expand(i, i)         # odd-length center at i
        l2, r2 = expand(i, i + 1)     # even-length center between i and i+1
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
    return s[best_l:best_r + 1]
```

**Solution** — Python ([Java](./LC-005-longest-palindromic-substring/lc-5/sol.java) · [C++](./LC-005-longest-palindromic-substring/lc-5/sol.cpp) · [Go](./LC-005-longest-palindromic-substring/lc-5/sol.go))

```python
# LC 5. Longest Palindromic Substring
from typing import Tuple


def longest_palindrome(s: str) -> str:
    """LC 5: longest contiguous palindromic substring of s.

    Expand around each of the 2n - 1 candidate centers (n character-centers
    plus n - 1 between-character centers). For each center, push outward
    while s[left] == s[right]; the loop terminates one step past the last
    valid match, so the maximal palindrome is s[left+1 : right] when the
    helper returns the corrected (left+1, right-1) pair.
    O(n^2) time, O(1) extra space.
    """
    if not s:
        return ""

    def expand(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    best_l, best_r = 0, 0
    for i in range(len(s)):
        l1, r1 = expand(i, i)            # odd-length center at i
        l2, r2 = expand(i, i + 1)        # even-length center between i and i+1
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
    return s[best_l:best_r + 1]
```

> **Interactive widget:** [Longest Palindromic Substring (LC 5) — expand around centers](../widgets/e-LC005-longest-palindrome.yml) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: on `s = "babad"`, the algorithm walks 9 centers (5 odd, 4 even). At i=1 the odd expansion finds `"bab"` and updates the running best to length 3. At i=2 the odd expansion finds `"aba"`, also length 3; strict `>` rejects the tie, so the answer stays `"bab"`. The remaining centers find nothing longer.*

The `expand` helper is the load-bearing piece. Its loop terminates when the pointers either disagree or fall off the string, which means the *last valid match* was the iteration before. Returning `(left + 1, right - 1)` corrects for that one over-step. The dual call `expand(i, i)` and `expand(i, i + 1)` is what handles odd-length and even-length centers without the input-doubling trick that Manacher's algorithm and the textbook "Slower algorithm" both use[^4].

Time `O(n²)`: each of `2n - 1` centers expands at most `n/2` steps, and the total work across all centers is bounded by `n²/2` by an arithmetic-series argument.[^4] Space `O(1)` extra. The widget animates the `"babad"` trace because that input surfaces the strict-vs-non-strict update guard — the tie at i=2 disappears on shorter inputs.

### Why this wins in practice over the table

Same asymptotic time. No allocation. No by-length fill order to memorize. Smaller constant: each iteration touches at most two characters and compares them; the table iteration touches three cells (`is_palin[i+1][j-1]`, `s[i]`, `s[j]`) and a write. The expand version stays in cache; the table version doesn't.

Manacher's algorithm gets to O(n) by exploiting palindrome mirroring: when a long palindrome centered at `c` already extends to the right boundary `r`, any position `i < r` inherits at least `min(r - i, p[mirror_of_i])` of its radius for free, amortizing total work to linear via a "center never decreases, right boundary only increases" potential.[^5] At `n = 1000` it is overkill; `10⁶` vs `10³` is sub-millisecond either way. The reason to know its name: at `n >= 10⁵`, expand-around-centers TLEs on the worst-case all-same input, and Manacher's becomes load-bearing rather than optional. The full code is roughly four times longer than the centers method and is rarely typed in a 35-minute interview. Naming the algorithm and sketching the mirroring intuition is the expected response.

## Edge cases

**Empty string.** LC's constraint guarantees `s.length >= 1`, but production-safe code short-circuits at `n == 0` to avoid an out-of-bounds read on `s[0]`. The Python reference returns `""` immediately; the four sibling implementations do the same.

**Even-length palindrome (`"abba"`, `"cbbd"`).** The classic catch for an odd-only implementation. `expand(i, i)` for any `i` finds at most a length-1 palindrome on `"cbbd"` (each character is a palindrome of itself); `expand(1, 2)` finds the length-2 `"bb"`. Without the second call, the algorithm returns a length-1 substring on inputs that have an even-length answer.

**All-same string (`"aaaa"`).** Every range is a palindrome, so the answer is the full string. The odd center at the middle index walks all the way to both boundaries; the algorithm's worst case for time is exactly this input, with each center expanding to half the string and total work at `n²/2` matching the bound.[^4]

## Common bugs

**Running only odd-length centers.** Calling `expand(s, i, i)` for every `i` and skipping `expand(s, i, i + 1)` returns one of `'c'`, `'b'`, `'d'` for `"cbbd"` and `'a'` for `"abba"`. The mental fix is the framing: a palindrome of even length anchors *between* two characters, not on one. Both anchorings are required.

**Returning `(left, right)` instead of `(left + 1, right - 1)`.** The expand loop's terminating condition is `s[left] != s[right]` or out-of-bounds. After the loop, `left` and `right` already point one step past the last valid match. Returning the raw `(left, right)` includes the mismatching characters; on `"cbbd"` the odd expansion at `i = 1` would report length 4 (the whole string) instead of length 1. Compute the corrected window inside `expand` once; the rest of the algorithm consumes it cleanly.

**Returning the length instead of the substring.** Tracking only `max_len` while iterating answers a different question. LC 5 wants the substring; track `(start, max_len)` together (or `(best_l, best_r)` as the reference does) and slice once at the end. The textbook longest-palindromic-*subsequence* DP recurrence in CLRS Problem 14-2 stores the scalar length in the cell[^3], which trains the wrong reflex for LC 5; the witness has to be tracked alongside.

**Computing length as `r - l - 1` after expansion.** When debugging an off-by-one, candidates often try to fix the `expand` return and then write `length = r - l - 1` somewhere downstream to "subtract back the over-step". Two corrections compound into a fresh bug. Pick one place to do the math (inside `expand`) and let the rest of the code work in true `[bestL, bestR]` coordinates.

## Interview follow-ups

**What if you need to count all palindromic substrings instead of returning the longest?** That's [LC 647](https://leetcode.com/problems/palindromic-substrings/). Same expand-around-centers template. For each center, increment a counter on every successful match instead of tracking the longest. `O(n²)` time, `O(1)` space, two-line modification of the reference. Amazon asks this one a lot.[^4]

**What about the longest palindromic *subsequence*?** Different problem despite the name collision: [LC 516](https://leetcode.com/problems/longest-palindromic-subsequence/). The substring (LC 5) requires endpoints to match AND the inner range to be a palindrome — strict AND, propagating "no" along the chain. The subsequence relaxes to `max(dp[i+1][j], dp[i][j-1])` when the endpoints disagree, because skipping one endpoint is allowed. On `"bbbab"`, LC 5 returns `"bbb"` (length 3, contiguous); LC 516 returns 4 (`"bbbb"`, skipping the `'a'`). LC 516 is the canonical CLRS Problem 14-2 / 15-2 setup[^3] and does NOT yield to expand-around-centers. The disambiguation is the question's whole point.

**How would you partition the string into palindromes?** That's [LC 131](https://leetcode.com/problems/palindrome-partitioning/), backtracking on top of a palindrome check. Precompute the `is_palin[i][j]` table from Approach 2 in O(n²), then enumerate partitions by recursing from each position to every later position where the prefix is a palindrome. The expensive piece is the partition enumeration (exponentially many in the worst case), not the palindrome predicate; this is where the table earns its keep.

**What if characters arrive one at a time?** This is the original Manacher framing. When the algorithm has to maintain "longest palindrome so far" at every prefix, expand-around-centers does not extend cleanly: each new character potentially invalidates work done for centers near the right edge. Manacher's 1975 paper title is "A new linear-time *on-line* algorithm for finding the smallest initial palindrome of a string"[^5]; the *on-line* qualifier is the entire interview answer. The right-boundary `r` and center `c` advance with each character at amortized O(1) cost.

## References

[^1]: LeetCode, "5. Longest Palindromic Substring." https://leetcode.com/problems/longest-palindromic-substring/

[^2]: walkccc, "LeetCode 5." https://walkccc.me/LeetCode/problems/5/

[^3]: walkccc, "CLRS Problem 15-2: Longest palindrome subsequence." https://walkccc.me/CLRS/Chap15/Problems/15-2/

[^4]: Wikipedia, "Longest palindromic substring." https://en.wikipedia.org/wiki/Longest_palindromic_substring

[^5]: Manacher, "A new linear-time on-line algorithm for finding the smallest initial palindrome of a string," JACM 22(3), 1975. https://doi.org/10.1145/321892.321896
