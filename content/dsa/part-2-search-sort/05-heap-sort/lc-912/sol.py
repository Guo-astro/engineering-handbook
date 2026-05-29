# LC 912. Sort an Array — heap-sort reference (in-place, O(n log n) worst case)
from typing import List


def heap_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    # Phase 1: Floyd's build-max-heap, right-to-left from last internal node.
    for start in range(n // 2 - 1, -1, -1):
        _sift_down(nums, start, n)
    # Phase 2: extract max repeatedly into the sorted suffix.
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        _sift_down(nums, 0, end)
    return nums


def _sift_down(a: List[int], root: int, end: int) -> None:
    """Restore max-heap property at `root`, assuming both child subtrees
    are valid max-heaps and the heap occupies indices [0, end)."""
    while True:
        left = 2 * root + 1
        if left >= end:
            return
        right = left + 1
        child = left
        if right < end and a[right] > a[left]:
            child = right
        if a[root] >= a[child]:
            return
        a[root], a[child] = a[child], a[root]
        root = child
