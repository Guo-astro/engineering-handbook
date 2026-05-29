# LC 912. Sort an Array
# Quicksort with median-of-three Lomuto partition.
from typing import List


def sort_array(nums: List[int]) -> List[int]:
    """LC 912: sort and return a new list. Input is not mutated."""
    arr = list(nums)
    if len(arr) > 1:
        _quicksort(arr, 0, len(arr) - 1)
    return arr


def _quicksort(arr: List[int], lo: int, hi: int) -> None:
    """In-place quicksort on arr[lo..hi] inclusive."""
    while lo < hi:
        # Median-of-three: place median(arr[lo], arr[mid], arr[hi]) into arr[hi].
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[lo]:
            arr[lo], arr[mid] = arr[mid], arr[lo]
        if arr[hi] < arr[lo]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[mid] < arr[hi]:
            arr[mid], arr[hi] = arr[hi], arr[mid]
        # arr[hi] now holds the median of the three; use it as Lomuto pivot.
        p = _lomuto_partition(arr, lo, hi)
        # Recurse on the smaller side; loop on the larger (Sedgewick tail-call fix).
        if p - lo < hi - p:
            _quicksort(arr, lo, p - 1)
            lo = p + 1
        else:
            _quicksort(arr, p + 1, hi)
            hi = p - 1


def _lomuto_partition(arr: List[int], lo: int, hi: int) -> int:
    """CLRS 4th ed. PARTITION: pivot is arr[hi]. Returns final pivot index."""
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1
