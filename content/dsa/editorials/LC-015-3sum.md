---
lc_id: 15
title: "3Sum"
slug: LC-015-3sum
primary_chapter: part-3-pointers-window-prefix/00-two-pointers-opposite
star: true
difficulty: medium
date_updated: 2026-05-25
languages: [python, java, cpp, go]
editorial_widget: e-LC015-3sum
---

# 3Sum

3Sum is the chapter where most candidates first meet duplicate-handling as a real algorithmic concern. The arithmetic is easy: fix one element, then it's 2Sum on the rest. The trick is reporting each unique triplet exactly once without a hash set, without a sorted-tuple canonicalization, and without slowing down the asymptotic bound. Three lines of pointer-skip discipline carry the entire chapter. The editorial below is mostly about those three lines.

The reduction is one sentence. Sort the array, fix an anchor `nums[i]`, and the inner sub-problem is "find every pair `(b, c)` with `b + c = -nums[i]`", which is [Two Sum](./LC-001-two-sum.md) on a sorted array. The `O(n^2)` total cost is asymptotically optimal in the comparison model, so once you've reduced to two pointers the work is correctness, not speed.

## The problem

Given an integer array `nums`, return every distinct triplet of values drawn from three different positions whose sum is zero. Two triplets are equal if they contain the same multiset of values regardless of order; the answer set must contain each distinct triplet exactly once. Constraints: `3 <= nums.length <= 3000`, `-10^5 <= nums[i] <= 10^5`. Difficulty Medium.[^1]

| Input | Expected | What it tests |
|---|---|---|
| `[-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]` | The classic case; two valid triplets, one shared anchor value |
| `[0, 0, 0]` | `[[0, 0, 0]]` | Three identical values produce one triplet, not three |
| `[0, 0, 0, 0]` | `[[0, 0, 0]]` | Four identical values still produce one triplet |
| `[1, 2, 3]` | `[]` | All-positive input; no triplet sums to zero |

The output is a list of **values**, not indices. That distinction is what makes 3Sum harder than [Two Sum](./LC-001-two-sum.md): a hash map keyed on indices does not naturally suppress value-equivalent triplets. The unique-triplet rule is the load-bearing constraint, and every approach below is graded on how cleanly it enforces uniqueness. Verbatim wording at [LC 15 3Sum](https://leetcode.com/problems/3sum/).

## Approach 1: brute force

Pick three indices `i < j < k`, check the sum, dedup by sorting each hit and storing it in a set.

```python
# Brute force: O(n^3) time, O(n^2) space — what we're replacing
def three_sum_brute(nums):
    seen = set()
    out = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    if triplet not in seen:
                        seen.add(triplet)
                        out.append(list(triplet))
    return out
```

The `tuple(sorted(...))` canonicalization is mandatory. Two triplets pulled from indices `(0, 3, 4)` and `(0, 4, 3)` are the same multiset but different ordered tuples; without the inner sort, both hash keys are distinct and duplicates leak through.

Time `O(n^3)`. Space `O(n^2)` worst case for the set. At `n = 3000` the brute force performs roughly `2.7 * 10^10` sum-checks and times out at LC's grader past about `n = 500`. The interview move is to write this anyway. It anchors the discussion, names the complexity out loud, and earns the "now let me speed this up" pivot that the rest of the conversation needs.

## Approach 2: hash set per anchor

The natural second instinct, and the one many candidates reach for after solving [Two Sum](./LC-001-two-sum.md) with a hash map. Sort the array, then for each anchor `i` run a Two Sum with target `-nums[i]` over the suffix using a hash set.

```python
# O(n^2) time, O(n) space — correct, but awkward at the edges
def three_sum_hash(nums):
    nums = sorted(nums)
    n = len(nums)
    out = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        seen = set()
        j = i + 1
        while j < n:
            complement = -nums[i] - nums[j]
            if complement in seen:
                out.append([nums[i], complement, nums[j]])
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
    return out
```

The reduction "3Sum equals anchor plus 2Sum" is the load-bearing insight; state it out loud. The hash version pays for it twice: extra `O(n)` space per anchor for the set, and a constant-factor slowdown versus array indexing in the sorted-pointer version. Worth writing once to confirm the reduction; not worth shipping.

## Approach 3: sort and two pointers (optimal)

Sort the array once. For each anchor `i`, place pointers `l = i + 1` and `r = n - 1` and converge them inward looking for `nums[l] + nums[r] == -nums[i]`. After every hit, advance both pointers and skip past any duplicates of the values just emitted, on both sides. The outer loop early-exits when `nums[i] > 0` because no triplet of values starting with a positive anchor sums to zero on a sorted array.

```python
def three_sum(nums):
    nums = sorted(nums)
    n = len(nums)
    out = []
    for i in range(n - 2):
        if nums[i] > 0:                              # early exit
            break
        if i > 0 and nums[i] == nums[i - 1]:         # (a) skip duplicate anchors
            continue
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:    # (b) skip dups on left
                    l += 1
                while l < r and nums[r] == nums[r + 1]:    # (c) skip dups on right
                    r -= 1
    return out
```

**Solution** — Python ([Java](./LC-015-3sum/lc-15/sol.java) · [C++](./LC-015-3sum/lc-15/sol.cpp) · [Go](./LC-015-3sum/lc-15/sol.go))

```python
# LC 15. 3Sum
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """LC 15: return every unique triplet of values summing to zero.

    Sort, then for each anchor i run a converging two-pointer sweep over the
    suffix targeting -nums[i]. Three duplicate-skip lines do all the work:
    skip equal anchors, and after each hit advance both pointers past their
    own value runs. O(n^2) time, O(1) auxiliary space (sort excluded).
    """
    nums = sorted(nums)
    n = len(nums)
    out: List[List[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return out
```

> **Interactive widget:** [3Sum (LC 15) — sort + anchor + opposite-ends with duplicate-skip](../widgets/e-LC015-3sum.yml) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: on `nums = [-1, 0, 1, 2, -1, -4]`, sort produces `[-4, -1, -1, 0, 1, 2]`. Anchor `-4` sweeps the suffix without a hit. Anchor `-1` at index 1 finds `(-1, 2)` then `(0, 1)`, emitting both triplets. Anchor `-1` at index 2 is skipped by rule (a). Anchors `0` and beyond contribute nothing. Final: `[[-1, -1, 2], [-1, 0, 1]]`.*

Time `O(n^2)`: outer loop is `O(n)` anchors, each inner sweep is `O(n)` because `r - l` shrinks by one every iteration. Space `O(1)` auxiliary (the sort's `O(log n)` stack is dominated by the outer-loop work and conventionally not counted). The bound matches the linear-decision-tree lower bound for 3SUM, so two-pointer is asymptotically optimal in the comparison model.[^2]

### Deduplication without a set

This is the section the rest of the editorial exists for. The two-pointer scaffold is straightforward; the three skip rules are not. Skip any one of them and the algorithm silently emits duplicate triplets on inputs you would not think to test.

There are exactly three skip points, in this order:

**(a) After picking anchor `i`.** If `i > 0 and nums[i] == nums[i-1]`, skip the inner sweep entirely. The previous anchor at this value already enumerated every triplet that contains it; running again would re-emit the same triplets with a different starting index. On `[-1, -1, 0, 1]`, anchor `-1` at index 0 finds `(0, 1)` and emits `[-1, 0, 1]`. Without the skip, anchor `-1` at index 1 would also find `(0, 1)` and emit `[-1, 0, 1]` again.

**(b) After a successful match, advance `l` past its run.** Once a triplet is emitted, `l += 1` moves to the next candidate. If that candidate has the same value as the position just used (`nums[l] == nums[l-1]`), the same triplet would be emitted again with a different inner partner on `r`. The `while` loop walks `l` forward until the value changes.

**(c) After a successful match, advance `r` past its run.** Symmetric to (b). The right side has the same problem in mirror image: a value run ending at the position just used would re-pair with the next `l` and emit the same triplet.

The invariant is the same in all three cases: after each guard fires, the active pointer sits at a value strictly different from any value already used in an emitted triplet at the current anchor. The case that surfaces all three failure modes is `[-2, -2, 0, 0, 2, 2]`: anchor `-2` at index 0 finds `(0, 2)` at `(l=2, r=4)` and emits `[-2, 0, 2]`. Without (b), the next iteration with `l=3` finds the same triplet because `r` slid one position and landed on a duplicate `2`. Without (c), the symmetric failure happens on the other side. Without (a), the second `-2` anchor re-enumerates everything. All three skips fit in seven lines of code, which is what keeps the algorithm at `O(n²)` time and `O(1)` extra space instead of paying the `O(n²)` set penalty.[^3]

A tempting alternative tracks the last emitted triplet's component values (`preva, prevb, prevc`) and refuses any new match. On `[-1, 0, 1, 2, -1, -4]` the algorithm emits `[-1, -1, 2]`, sets `preva = -1`, then refuses to emit `[-1, 0, 1]` because the new anchor value also equals `preva`. The fix is to drop the value-tracking and use the position-based skips above.[^3]

## Edge cases

**`n < 3`.** The outer loop `range(n - 2)` is empty and the function returns `[]`. The constraint `3 <= nums.length` puts this just outside the in-range corner, but the algorithm handles it cleanly without a guard.

**All zeros: `[0, 0, 0]`.** Anchor `i = 0` (value 0) sets `target = 0` and finds `(0, 0)` immediately at `(l = 1, r = 2)`, emitting `[0, 0, 0]`. Both inner skips fire as no-ops because `l = 2 > r = 1` exits the inner loop. Anchor `i = 1` triggers rule (a) and is skipped. The algorithm emits exactly one triplet, not three or five.

**No solution: `[1, 2, 3]`.** The early-exit `if nums[i] > 0: break` fires on the first iteration. The inner sweep never runs. Returns `[]` in `O(1)` after the sort.

## Common bugs

**Missing the right-pointer dedup.** Most submissions get rule (a) and rule (b) and forget rule (c). Test on `[-2, -2, 0, 0, 2, 2]`; the algorithm should emit `[-2, 0, 2]` exactly once, not twice.

**Using `set(tuple(sorted([a, b, c])))` to dedup.** Correct, and a graceful fallback if the position-based skips feel fragile under interview pressure. The cost is `O(n²)` extra space and a 2-3× constant-factor slowdown. Senior interviewers grade this as "almost there"; the in-place dedup is what 3Sum specifically tests for.

**Using `>=` instead of `>` in the early-exit.** Writing `if nums[i] >= 0: break` skips the all-zero case. On `[0, 0, 0]` the first anchor has value 0, the rule fires, and the function returns `[]` instead of `[[0, 0, 0]]`. The correct rule is strict.

**Worrying about integer overflow on `nums[l] + nums[r]`.** Not a concern here. With `|nums[i]| <= 10⁵`, the pair sum fits in 32-bit signed `int` with margin. The Java and C++ implementations need no `long` cast. [LC 18 4Sum](https://leetcode.com/problems/4sum/) does require it because its constraint is wider.

## Interview follow-ups

**What about 4Sum?** That's [LC 18](https://leetcode.com/problems/4sum/). Same template, one extra outer loop. Fix two anchors and run the inner two-pointer sweep on the suffix targeting `T - nums[i] - nums[j]`. Two layers of duplicate-skip on the outer side, plus the same `(b)` and `(c)` rules from this editorial unchanged. Total cost `O(n³)`. Generalizes to k-Sum at `O(n^(k-1))`.

**What if the goal is the closest sum, not exactly the target?** That's [LC 16 — 3Sum Closest](https://leetcode.com/problems/3sum-closest/). Same algorithm, different objective: find the triplet whose sum is closest to a given target. Drop all three duplicate-skip rules (you only need one closest-sum, not all unique triplets) and replace the equality branch with "compute `|s - T|`; if it improves the running minimum, update." Same `O(n²)` cost.

**What about counting triplets below a target?** That's [LC 259 — 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/). The dedup discipline disappears because the count is over indices, not values. When `nums[i] + nums[l] + nums[r] < target`, every pair `(l, l+1), (l, l+2), ..., (l, r)` satisfies the condition because the array is sorted, so add `r - l` to the count and advance `l`. Same `O(n²)`.

**Is there a lower bound on this problem's time complexity?** The two-pointer `O(n²)` matches the linear-decision-tree lower bound proved by Erickson in 1999.[^2] Whether 3Sum admits a truly subquadratic algorithm in the word-RAM model is open; Pătrașcu's 3SUM-hardness conjecture is the load-bearing assumption underneath dozens of fine-grained complexity reductions.[^4]

## References

[^1]: doocs/leetcode, "LC 15 3Sum." https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0015.3Sum/README_EN.md

[^2]: Wikipedia, "3SUM." https://en.wikipedia.org/wiki/3SUM

[^3]: Stack Overflow, "Leetcode #15: 3sum, avoiding duplicate," 2016. https://stackoverflow.com/questions/38909591/leetcode-15-3sum-avoiding-duplicate

[^4]: Pătrașcu, "Towards polynomial lower bounds for dynamic problems," STOC 2010. https://doi.org/10.1145/1806689.1806772
