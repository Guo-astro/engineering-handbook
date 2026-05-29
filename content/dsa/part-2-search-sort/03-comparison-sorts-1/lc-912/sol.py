# LC 912. Sort an Array (canonical merge sort, top-down with shared aux buffer)
"""Merge sort, top-down, stable.

The merge step uses `<=` (not `<`) when comparing left[i] vs right[j], which
guarantees stability: equal keys from the left half are emitted before equal
keys from the right half. CLRS 4th ed. §2.3.1 calls this the stable-merge
invariant; Sedgewick algs4 §2.2 makes the same observation.
"""
from __future__ import annotations
import sys
from typing import List

sys.setrecursionlimit(10**6)  # top-level once, not per-call.


def sort_array(nums: List[int]) -> List[int]:
    """Sort `nums` in non-decreasing order using merge sort. Returns a new list."""
    if len(nums) <= 1:
        return list(nums)
    arr = list(nums)
    aux = [0] * len(arr)  # single shared scratch buffer
    _merge_sort(arr, aux, 0, len(arr) - 1)
    return arr


def _merge_sort(arr: List[int], aux: List[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2  # Bloch 2006: avoid (lo + hi) // 2 to dodge overflow.
    _merge_sort(arr, aux, lo, mid)
    _merge_sort(arr, aux, mid + 1, hi)
    if arr[mid] <= arr[mid + 1]:
        return  # already in order; Sedgewick algs4 §2.2.2 short-circuit
    _merge(arr, aux, lo, mid, hi)


def _merge(arr: List[int], aux: List[int], lo: int, mid: int, hi: int) -> None:
    # Copy the slice into aux so we can write back into arr in-place.
    for k in range(lo, hi + 1):
        aux[k] = arr[k]
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if aux[i] <= aux[j]:  # `<=` makes the merge stable.
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
        k += 1
    while i <= mid:
        arr[k] = aux[i]
        i += 1
        k += 1
    while j <= hi:
        arr[k] = aux[j]
        j += 1
        k += 1
