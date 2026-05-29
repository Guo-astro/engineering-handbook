"""LC 33, LC 153, LC 162: binary-search variants on non-trivially-sorted input,
plus lower_bound / upper_bound on duplicate-bearing sorted arrays and the
parametric-search template (binary search on the answer).

The closed-interval and half-open invariants from chapter 2.1 carry through.
What changes per variant is which comparison drives the halving decision.
"""
from typing import Callable, List


def lower_bound(nums: List[int], target: int) -> int:
    """Smallest index i with nums[i] >= target, or len(nums) if none.

    Half-open [lo, hi). Invariant: every j < lo has nums[j] < target;
    every k >= hi has nums[k] >= target. Comparison: nums[mid] < target.
    On [1, 2, 2, 2, 3] target 2 returns 1 (leftmost 2).
    """
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    """Smallest index i with nums[i] > target, or len(nums) if none.

    Same skeleton as lower_bound; the comparison is nums[mid] <= target,
    which flips equality to the left of the boundary instead of the right.
    On [1, 2, 2, 2, 3] target 2 returns 4 (one past the rightmost 2).
    The count of equal keys is upper_bound(t) - lower_bound(t).
    """
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated(nums: List[int], target: int) -> int:
    """LC 33. Exact match in a rotated sorted array (distinct values).

    Closed [lo, hi]. At each step exactly one of [lo..mid] and [mid..hi]
    is sorted; test target against the sorted half's endpoints and recurse
    into the half whose range contains target.
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # overflow-safe per Bloch 2006
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            # Left half [lo..mid] is sorted.
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # Right half [mid..hi] is sorted.
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def find_min_rotated(nums: List[int]) -> int:
    """LC 153. Minimum in a rotated sorted array of unique elements.

    Compare nums[mid] with the right endpoint nums[hi]: if mid is larger,
    the rotation point is strictly right of mid; otherwise mid is itself
    a candidate, so keep it on the left.
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def find_peak_element(nums: List[int]) -> int:
    """LC 162. Index of any strict peak (boundary sentinels -infinity).

    Slope at mid: nums[mid] > nums[mid+1] means a peak is in [lo..mid];
    nums[mid] < nums[mid+1] means a peak is in [mid+1..hi]. The boundary
    sentinels guarantee at least one peak exists in any half.
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bs_on_answer_min(lo: int, hi: int, feasible: Callable[[int], bool]) -> int:
    """Binary search on the answer: smallest X in [lo, hi] with feasible(X)
    true. feasible must be monotone (once true at X, true for every X' >= X).
    Returns hi + 1 if no X in [lo, hi] is feasible.
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo if feasible(lo) else hi + 1
