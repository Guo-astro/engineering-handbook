# LC 704. Binary Search. Exact-match closed-interval template.
# LC 35. Search Insert Position. Lower-bound half-open template.
# LC 278. First Bad Version. Predicate-driven half-open template.
#   LC 704: ([-1,0,3,5,9,12], 9) -> 4; ([-1,0,3,5,9,12], 2) -> -1;
#           ([5], 5) -> 0; ([5], -5) -> -1; ([1,3,5,7,9,11,13], 7) -> 3; ([], 1) -> -1.
#   LC 35: ([1,3,5,6], 5) -> 2; ([1,3,5,6], 2) -> 1; ([1,3,5,6], 7) -> 4; ([1,3,5,6], 0) -> 0.
#   LC 278: n=5,bad=4 -> 4; n=1,bad=1 -> 1; n=INT_MAX,bad=1702766719 -> 1702766719.

from typing import Callable, List


def search(nums: List[int], target: int) -> int:
    """LC 704. Exact-match closed-interval template.

    Loop invariant: target, if it exists, is in nums[lo..hi] (both inclusive).
    Loop terminates when lo > hi (interval empty, target not present).
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # overflow-safe vs (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_insert(nums: List[int], target: int) -> int:
    """LC 35. Lower-bound (leftmost insertion point) template.

    Loop invariant: every index j with j < lo satisfies nums[j] < target;
    every index k with k >= hi satisfies nums[k] >= target.
    Terminates when lo == hi; lo is the insertion point.

    Uses half-open style: [lo, hi) with hi = len(nums) (one past the end).
    """
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def first_bad_version(n: int, is_bad_version: Callable[[int], bool]) -> int:
    """LC 278. Predicate-driven leftmost template on [1, n].

    Loop invariant: the answer (first bad version), which exists by problem
    guarantee, lies in [lo, hi]. At loop exit lo == hi == answer.
    """
    lo, hi = 1, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_bad_version(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
