---
lc_id: 1
title: "Two Sum"
slug: LC-001-two-sum
primary_chapter: part-1-linear-data-structures/03-hash-maps
star: true
difficulty: easy
date_updated: 2026-05-25
languages: [python, java, cpp, go]
editorial_widget: e-LC001-two-sum
---

# Two Sum

LC 1 is the most-submitted problem on LeetCode and the most common opening question in technical screens. The algorithm is four lines. The interview is everything around those four lines: write the brute force, name its complexity, propose the optimization, write it cleanly. In that order.

The lesson is one sentence. When an inner loop searches for one specific value, a hash map of "value to index" replaces the loop with an O(1) average probe. Everything else here is the order of operations and the duplicate-value case that exposes when you got the order wrong.

## The problem

Given an integer array `nums` and an integer `target`, return the two array positions whose values sum to `target`. Exactly one valid pair exists; the same position cannot be used twice; either order is accepted. Constraints sit at small Easy scale: `2 <= nums.length <= 10⁴`, every value and the target between -10⁹ and 10⁹.[^1]

The follow-up on the LC page is the entire reason this problem exists: *can you do it in less than O(n²)?* Without that prompt it's a one-line nested loop and the interview is over.

| Input | Expected | What it tests |
|---|---|---|
| `[2, 7, 11, 15]`, target `9` | `[0, 1]` | The classic case |
| `[3, 2, 4]`, target `6` | `[1, 2]` | Skips index 0 |
| `[3, 3]`, target `6` | `[0, 1]` | Duplicate value matched against the **earlier** occurrence, not against itself |

That last row breaks most first attempts at the optimized version. Hold it in mind. Verbatim wording at [LC 1 Two Sum](https://leetcode.com/problems/two-sum/).

## Approach 1: brute force

Translate the statement directly. Pick `i < j`, check `nums[i] + nums[j] == target`, return the first hit.

```python
# Brute force: O(n²) — what we're replacing
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

Inner bound is `j > i`, not `j != i`. The first formulation visits every unordered pair exactly once and guarantees distinct positions by construction; the second needs a post-hoc filter and signals "I patch wrong algorithms" rather than "I write right ones."

Time O(n²), space O(1). At `nums.length = 10⁴` the worst case runs roughly 5 × 10⁷ comparisons, which is borderline in C++ and times out in Python on the hidden cases.[^1] Saying *"this is O(n²); the follow-up wants better"* out loud is the calibration line the next conversation needs.

## Approach 2: sort and two pointers

The natural second instinct, and the wrong turn worth naming. If the array is sorted, the sum is monotone in pointer positions: increment left to grow it, decrement right to shrink it.

```python
# Wrong turn: O(n log n), but breaks LC 1 as stated
def two_sum_sort(nums, target):
    nums_sorted = sorted(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums_sorted[l] + nums_sorted[r]
        if s == target:
            return [l, r]   # WRONG: sorted indices, not original
        l, r = (l + 1, r) if s < target else (l, r - 1)
    return []
```

The function runs and returns a length-2 array. It does not solve LC 1, because LC 1 asks for original indices and `sorted` destroys the mapping. On `[3, 2, 4]` with target 6, the sorted view is `[2, 3, 4]`, the pointers find `2 + 4 = 6` at sorted positions `(0, 2)`, and the function returns `[0, 2]`. The correct answer is `[1, 2]`.

The fix is to sort `(value, original_index)` tuples. That works and is exactly the canonical solution to [LC 167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), where the input is already sorted and the constant-extra-space rule forbids a hash map.[^2] On LC 1 it is strictly worse than the hash map: O(n log n) versus O(n) average, plus the tuple allocation. A candidate who proposes the sort, immediately catches the index-destruction wrinkle, and pivots to a hash map demonstrates fluency in the trade-off space, which is the conversation this approach exists to invite.

## Approach 3: one-pass hash map (optimal)

The brute force's inner loop searches for one value: the **complement** `target - nums[i]`. A hash map answers "have I seen this value, and at what index?" in O(1) average. Replace the search with a probe; the algorithm collapses from O(n²) to O(n).

This is the textbook reduction in Sedgewick & Wayne §3.4: when the inner work of a doubly-nested loop is a search for one key, a hash table replaces the entire inner loop with a single probe.[^3] Two questions matter as `i` walks the array:

1. Is `target - nums[i]` already recorded? If yes, the partner index is in the map; return both.
2. If not, record `nums[i] -> i` and continue.

```python
def two_sum(nums, target):
    seen = {}                              # value -> first-seen index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]   # lookup BEFORE store
        seen[x] = i
    return []
```

**Solution** — Python ([Java](./LC-001-two-sum/lc-1/sol.java) · [C++](./LC-001-two-sum/lc-1/sol.cpp) · [Go](./LC-001-two-sum/lc-1/sol.go))

```python
# LC 1. Two Sum
from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    """LC 1: return indices of two numbers in nums summing to target.

    One pass with a value -> first-seen-index map. For each x, look up the
    complement (target - x) BEFORE inserting x; the lookup-then-insert order
    is what prevents matching an element against itself on inputs like [3, 3].
    O(n) average time, O(n) space.
    """
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
```

> **Interactive widget:** [Two Sum (LC 1) — optimal one-pass hash map](../widgets/e-LC001-two-sum.yml) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: with `nums = [3, 3]`, target 6, iteration 0 looks up complement 3 against an empty map (miss) and stores `3 -> 0`. Iteration 1 looks up complement 3 against `{3: 0}` (hit) and returns `[0, 1]`.*

The widget plays the trace on `[3, 3]` because it is the only one of LC's three examples that exercises the lookup-before-store invariant. On the other two, the map fills with three distinct values before the answer is found and either ordering works; the bug from reversing the order stays hidden.

### Why one pass beats two passes

A two-pass variant builds the full `value -> index` map first, then scans for complements. Same O(n) time, same O(n) space.

```python
# Two-pass variant — equivalent, but walks twice
def two_sum_two_pass(nums, target):
    seen = {nums[i]: i for i in range(len(nums))}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen and seen[complement] != i:
            return [i, seen[complement]]
    return []
```

Pass 1's dict comprehension overwrites earlier indices with later ones, so on `[3, 3]/6` the map ends up `{3: 1}`. The `seen[complement] != i` guard prevents a `[0, 0]` answer when `i = 0` looks up its own complement. The one-pass version is the interview default: one loop instead of two, the same memory, and the same O(n) bound, with one less invariant to state.

## Edge cases

**Duplicate values, both in the answer.** `[3, 3]`, target 6. The constraint forbids using the same **index** twice, not the same **value** twice. Reversing lookup and store on the optimized version produces `[0, 0]` — a same-value-against-itself match — which is the most common bug on this approach.

**Negative integers.** `[-1, -2, -3, -4]`, target -3. The algorithm is sign-agnostic; `target - x` works for any signed integer. Defensive `if x > target: continue` filters break on negative inputs and sometimes appear from candidates assuming a non-negative target.

**Integer overflow on the complement.** Python's integers are arbitrary precision; non-issue. Java, C++, and Go use 32-bit `int` on most platforms. Worst-case `target - nums[i]` is `10⁹ - (-10⁹) = 2 × 10⁹`, which fits in a signed 32-bit int (max ~2.147 × 10⁹) with margin.[^1] No `long` cast needed.

## Common bugs

**Returning `[0, 0]` on `[3, 3]/6`.** The classic. The candidate writes `seen[nums[i]] = i` *before* `if complement in seen`, so on iteration 0 the map already contains `{3: 0}` when the complement check runs. Lookup first, store second.

**Returning values instead of indices.** On `[2, 7, 11, 15]/9` the candidate returns `[2, 7]` instead of `[0, 1]`. Reading the problem statement — *"return the indices"* — is the fix.

**Hash *set* instead of hash *map*.** Set membership answers "have I seen this value" but discards the index. The candidate finishes with the right pair of values and the wrong pair of indices.

**Java boxing on the hot path.** `HashMap<Integer, Integer>` autoboxes both key and value on every `put` and `get`. At LC 1's max input that is 10⁴ allocations on the worst-case path: fine for one-shot submission, painful for a production map at high QPS. The production fix is a primitive-keyed map like Eclipse Collections' `IntIntHashMap`. An interviewer asking "is there a faster version" is signaling this upgrade.[^4]

## Interview follow-ups

**What if the input is sorted?** The hash map is no longer the right tool. Two pointers from opposite ends solve it in O(n) time and O(1) space, better on space than the hash map. This is [LC 167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), and the pivot is the highest-leverage pattern signal in the entire pointer-window family: sorted input unlocks two pointers.[^2]

**What if there are multiple valid pairs?** The single-hit version short-circuits; an all-pairs version cannot. Either keep iterating after a hit and append every match, or build a `value -> list-of-indices` map and enumerate the cross product of `seen[x]` and `seen[target - x]`, taking care when `x == target - x` to avoid double-counting.

**What if the input is too large for memory?** Two cost regimes. Disk-resident array: external-sort and run the LC 167 two-pointer scan with streaming reads from each end. True stream that cannot be re-read: build a hash set incrementally, check each new element's complement against it as it arrives. The streaming version is essentially [LC 170 Two Sum III](https://leetcode.com/problems/two-sum-iii-data-structure-design/), trading fast `add` for slower `find` versus the reverse.

**What about Three Sum?** Fix `nums[i]` and run Two Sum on the remaining array with target `-nums[i]`, giving O(n²). The canonical solution sorts and runs two pointers per anchor: same O(n²), with clean duplicate-suppression by skipping equal anchors and equal pointer positions. The pivot from "unsorted, return indices, hash map" to "sorted, return values, two pointers, dedup" is what this family teaches. Deep treatment in the [3Sum editorial](./LC-015-3sum.md).

**What's the worst-case versus expected complexity?** Hash-map Two Sum is O(n²) worst case under adversarial collisions and O(n) expected under simple uniform hashing, the bound CLRS Theorem 11.1 gives.[^5] In production, mitigations exist: Java 8 treeifies a chain at length 8, bounding the worst case at O(n log n); Python's dict uses open addressing with perturbation that defeats the simplest collision attacks. The interviewer is checking whether the candidate distinguishes the bound that is proved from the bound that ships.

## References

[^1]: doocs/leetcode, "LC 1 Two Sum." https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0001.Two%20Sum/README_EN.md

[^2]: doocs/leetcode, "LC 167 Two Sum II — Input Array Is Sorted." https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0167.Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted/README_EN.md

[^3]: Sedgewick and Wayne, *Algorithms*, 4th ed., Addison-Wesley, 2011, §3.4. https://algs4.cs.princeton.edu/34hash/

[^4]: walkccc, "LeetCode 0001." https://walkccc.me/LeetCode/problems/0001/

[^5]: Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*, 4th ed., MIT Press, 2022, Ch. 11.
