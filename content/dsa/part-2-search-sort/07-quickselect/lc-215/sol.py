# LC 215. Kth Largest Element in an Array
import random
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """LC 215. Return the k-th largest element (1-indexed)."""
    target = len(nums) - k
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        pivot_idx = _partition(nums, lo, hi)
        if pivot_idx == target:
            return nums[pivot_idx]
        if pivot_idx < target:
            lo = pivot_idx + 1
        else:
            hi = pivot_idx - 1
    return -1  # unreachable for valid 1 <= k <= len(nums)


def _partition(nums: List[int], lo: int, hi: int) -> int:
    """Lomuto partition with a uniformly random pivot."""
    rand_idx = random.randint(lo, hi)
    nums[rand_idx], nums[hi] = nums[hi], nums[rand_idx]
    pivot = nums[hi]
    store = lo
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[store], nums[i] = nums[i], nums[store]
            store += 1
    nums[store], nums[hi] = nums[hi], nums[store]
    return store
