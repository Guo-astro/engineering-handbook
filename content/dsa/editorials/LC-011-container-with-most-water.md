---
lc_id: 11
title: "Container With Most Water"
slug: LC-011-container-with-most-water
primary_chapter: part-3-pointers-window-prefix/00-two-pointers-opposite
star: true
difficulty: medium
date_updated: 2026-05-25
languages: [python, java, cpp, go]
editorial_widget: e-LC011-container
---

# Container With Most Water

LC 11 is the cleanest case-analysis proof anywhere in the two-pointer family. The algorithm is six lines. The interview is the line you have to argue out loud: *advancing the taller pointer cannot help*. That sentence is the entire problem; everything else is implementation.

## The problem

Given an integer array `height` of length `n`, treat each entry as a vertical wall standing on the x-axis at index `i`. Pick any two indices `i < j`. The water held between those walls is bounded by the *shorter* wall and runs the full distance between them, so the area is `min(height[i], height[j]) * (j - i)`. Return the maximum such area over all pairs. Constraints: `2 <= n <= 10⁵`, `0 <= height[i] <= 10⁴`.[^1]

| Input | Expected | What it tests |
|---|---|---|
| `[1, 8, 6, 2, 5, 4, 8, 3, 7]` | `49` | The classic case; optimal pair is `(1, 8)` for `min(8, 7) * 7` |
| `[1, 1]` | `1` | Minimum `n`; width is `1`, not `2` |
| `[4, 3, 2, 1, 4]` | `16` | Equal walls at the ends; the gap between them is the answer |

Verbatim wording at [LC 11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/).

## Approach 1: brute force

Translate the statement directly. Loop over every unordered pair `i < j`, compute the area, keep the best.

```python
# Brute force: O(n²) — what we're replacing
def max_area_brute(height):
    n = len(height)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            if area > best:
                best = area
    return best
```

Correct on all inputs, dead on the ones the grader cares about. At `n = 10⁵` the inner loop body runs roughly `n * (n - 1) / 2 ≈ 5 × 10⁹` times. LC's per-test budget is about a second, which buys somewhere around `10⁸` simple operations in Python and a few times that in C++. Past `n ≈ 10⁴` the grader times out. Saying *"this is `O(n²)`; the constraints want `O(n)`"* before writing the optimization is the interview signal.

## Approach 2: two pointers (optimal)

Start with one pointer at each end of the array. Compute the candidate area. Advance the pointer at the strictly shorter wall by one; on ties, advance either (the canonical convention, used by the four reference implementations, is to advance the right pointer in the `else` branch). Repeat until the pointers cross.

```python
def max_area(height):
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        h = min(height[l], height[r])
        if h * (r - l) > best:
            best = h * (r - l)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
```

**Solution** — Python ([Java](./LC-011-container-with-most-water/lc-11/sol.java) · [C++](./LC-011-container-with-most-water/lc-11/sol.cpp) · [Go](./LC-011-container-with-most-water/lc-11/sol.go))

```python
# LC 11. Container With Most Water
from typing import List


def max_area(height: List[int]) -> int:
    """LC 11: maximum water held between two walls in `height`.

    Two pointers, opposite ends. At each step, compute the candidate area
    `min(h[l], h[r]) * (r - l)`, then advance the pointer at the strictly
    shorter wall (ties: advance the right pointer, by convention). The
    case-analysis proof is in the editorial: advancing the taller wall
    cannot improve the answer because the shorter wall still binds and
    the width strictly shrinks. O(n) time, O(1) space.
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h_l, h_r = height[left], height[right]
        width = right - left
        if h_l < h_r:
            area = h_l * width
            if area > best:
                best = area
            left += 1
        else:
            area = h_r * width
            if area > best:
                best = area
            right -= 1
    return best
```

> **Interactive widget:** [Container With Most Water (LC 11) — greedy two-pointer shrink](../widgets/e-LC011-container.yml) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: on `[1, 8, 6, 2, 5, 4, 8, 3, 7]`, step 1 places pointers at indices 0 and 8 (heights 1 and 7) and computes area 8. Step 2 advances `l` to 1 (height 8) and computes `min(8, 7) * 7 = 49` — the optimal answer. The remaining six steps sweep `r` leftward and never beat 49; the loop terminates when the pointers cross.*

The loop runs at most `n - 1` iterations because each step advances exactly one pointer by one. Time `O(n)`, space `O(1)`. On `n = 10⁵` it finishes in single-digit milliseconds.[^2]

### Why moving the taller pointer never helps

The case analysis is short, but the order of the steps matters. Write it out once; you will not need to write it out again.

Suppose the pointers are at `(l, r)` with `height[l] < height[r]`. The candidate area is `min(height[l], height[r]) * (r - l) = height[l] * (r - l)` because the left wall is the shorter and binds the height.

Two moves are available. Either advance `r` inward by one (toward smaller indices), or advance `l` inward by one (toward larger indices). Consider what each does to the candidate area at the new pair.

**Move `r` inward, leave `l` fixed.** The new pair is `(l, r')` for some `r' < r`. The new width is `r' - l`, strictly less than `r - l`. The new height bound is `min(height[l], height[r'])`. There are two cases for the right wall's new height:

- `height[r'] >= height[l]`. The bound stays at `height[l]` (the left wall still binds). New area is `height[l] * (r' - l) < height[l] * (r - l)`. Strictly worse.
- `height[r'] < height[l]`. The bound drops to `height[r']`, which is strictly less than `height[l]`. New area is `height[r'] * (r' - l)`. The bound shrank and the width shrank; new area is strictly less than `height[l] * (r - l)`. Also strictly worse.

In both cases, regardless of what `height[r']` turns out to be, the area can only decrease. Holding `l` fixed and walking `r` inward visits a sequence of pairs each one of which is strictly worse than the current pair. None can beat what we already have.

**Move `l` inward, leave `r` fixed.** The new pair is `(l', r)` for some `l' > l`. The new width is `r - l'`, strictly less. The new height bound is `min(height[l'], height[r])`. If `height[l'] <= height[l]`, the bound is at most `height[l]` and the area is at most `height[l] * (r - l')`, strictly less than the current. But if `height[l'] > height[l]`, the height bound *climbs*. It is now bounded by whichever of `height[l']` and `height[r]` is smaller, both of which exceed `height[l]`. Whether the area grows depends on whether the height gain offsets the width loss. The point is that it *can* grow. Advancing `l` is the only move with that property.

So at every state, advancing the shorter pointer is the only direction in which the answer can improve. Advancing the taller pointer is dominated: the abandoned pair is no better than what we just had, and every subsequent pair on that side is also no better. We can throw away every pair `(l, r')` for `r' < r` without checking them and still find the optimum, because none of them can hold more water than `(l, r)`. The symmetric argument holds when `height[l] > height[r]`.

The key word is *dominated*. The proof does not say advancing the shorter wall is the move that finds the optimum; it says advancing the taller wall is the move that *cannot* find anything better than what we already have. The algorithm proceeds by elimination: at each step we discard a half-line of the search space (every pair on the taller-wall side of the abandoned pointer) because the proof guarantees the optimum is not in there.

This is the same exchange-argument shape that makes activity-selection greedy correct in CLRS Chapter 16: at each step, prove the locally greedy move is dominated by no other, and the global optimum follows by induction.[^3]

## Edge cases

**Minimum `n = 2`.** Inputs like `[1, 1]` or `[5, 3]` have a single pair to evaluate. The width is `j - i = 1`, not `2`; the bars sit at indices 0 and 1, and the gap between them is one unit. `[1, 1]` returns `1`; `[5, 3]` returns `3`. The grader catches the off-by-one width on this case immediately.

**Equal heights.** Inputs like `[5, 5, 5]` have no strict shorter wall on the first compare. The algorithm's `else` branch fires and advances `r` (the canonical implementations use strict `<`, so equality falls through to advance the right pointer). Advancing either pointer is correct; the symmetric argument in the proof covers the tie under "advance the shorter, where ties count as shorter."[^4] Both directions reach the same answer.

**Strictly decreasing heights.** On `[5, 4, 3, 2, 1]` the right wall is always shorter, so every iteration advances `r`. The first probe at `(0, 4)` gives `min(5, 1) * 4 = 4`; the optimum lands at `(0, 3)` for `min(5, 2) * 3 = 6`. Monotone arrays degenerate to a single-direction sweep.

## Common bugs

**Width as `r - l + 1`.** The most common LC 11 mistake. Walls sit at integer x-coordinates and have zero thickness; the water between them is the geometric *gap*, not the count of cells they bracket. On `[1, 1]` the wrong formula returns `2`; the grader rejects on the first hidden test. Fix: width is `r - l`, always.

**Advancing both pointers when the heights are equal.** The canonical algorithm advances only one pointer per iteration: the right pointer, on ties. Advancing both on a tie is wrong on inputs where the optimum is one step away from the tie state on the side you discarded. On `[5, 1, 5]` the initial pair `(0, 2)` ties at heights 5 and 5 with area `5 * 2 = 10`; advancing both lands at `l = r = 1` and the loop exits without checking the pair `(0, 1)` or `(1, 2)`. Advancing only one keeps the search alive and returns the same `10`. Either single-pointer advance works; both-pointer advance does not.

**Advancing the taller pointer.** A reader who skips the proof and tries the symmetric variant (advance the taller wall) will write code that fails on the first non-symmetric test. On `[1, 8, 6, 2, 5, 4, 8, 3, 7]`, advancing the taller wall at step 1 means `r` moves from index 8 to index 7 (height 3), abandoning the wall of height 7 that is part of the optimal pair. The algorithm returns 16, not 49. The proof exists to prevent this exact mistake; reading the proof is cheaper than debugging it.

**Updating `best` only on strict improvement.** Writing `if area > best` is correct (the problem asks for the maximum, and equal-to-current updates are no-ops); writing `if area >= best` is also correct but redundant. The bug to watch is the inverse: forgetting to compare at all and assigning `best = area` unconditionally. On any input where a later iteration's area is smaller than `best`, the unconditional assignment overwrites the correct answer with garbage.

## Interview follow-ups

**What about Trapping Rain Water?** The natural Hard follow-up is [LC 42](https://leetcode.com/problems/trapping-rain-water/), which looks like the same problem and is not. LC 42 sums the water trapped *above each individual cell*, not the water held between two specific walls. The two-pointer scaffold carries over — pointers at the ends, advance the shorter side — but the per-cell formula is `min(left_max, right_max) - height[i]`, with running maxes maintained as the pointers walk inward. Same family, harder bookkeeping; the LC 11 proof is the warm-up for the LC 42 proof.[^2]

**How would you return the actual indices, not just the area?** Maintain `best_l` and `best_r` alongside `best`, updating them on every strict improvement. The algorithm's structure does not change; the bookkeeping does. Most interviewers ask this version after you finish the area version, to check whether you understand which pair you found.

**What if the bars arrive as a stream?** Two pointers needs random access to both ends; a left-to-right stream cannot place the right pointer when the second bar arrives. The streaming reformulation is a different problem that maintains a monotone structure of "candidate left walls that might still pair with a future right wall," normally solved with a monotonic stack. The interview signal is recognizing that random access is a precondition of the two-pointer family, not an incidental detail.

## References

[^1]: doocs/leetcode, "LC 11 Container With Most Water." https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0011.Container%20With%20Most%20Water/README_EN.md

[^2]: NeetCode, "Container With Most Water." https://neetcode.io/problems/max-water-container

[^3]: Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*, 4th ed., MIT Press, 2022, Ch. 16 (greedy algorithms).

[^4]: scanny et al., "Proof for LeetCode 11," CS Stack Exchange, 2020. https://cs.stackexchange.com/questions/121472/proof-for-leetcode-11-container-with-most-water-problem
