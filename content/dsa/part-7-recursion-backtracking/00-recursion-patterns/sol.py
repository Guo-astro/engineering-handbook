# Chapter 7.0 — Recursion patterns: linear, tree, and divide-and-conquer
# merge_sort canonical cases pass.
import sys
from functools import lru_cache
from typing import List

# CPython default recursion limit is 1000; bump for deep traces and tree recursion.
sys.setrecursionlimit(10**6)


# Shape 1: linear recursion. One self-call per frame, depth n, work O(n).
# Tail-recursive form; CPython does NOT eliminate tail calls.
def fib_linear(n: int, a: int = 0, b: int = 1) -> int:
    """Linear recursion: T(n) = T(n-1) + O(1)."""
    if n == 0:
        return a
    return fib_linear(n - 1, b, a + b)


# Shape 2: tree recursion. Two self-calls per frame; T(n) = T(n-1) + T(n-2) + O(1).
# Total frames Theta(phi^n) where phi is the golden ratio (~1.618).
def fib_tree(n: int) -> int:
    """Un-memoized tree recursion: exponential without a cache."""
    if n < 2:
        return n
    return fib_tree(n - 1) + fib_tree(n - 2)


# Shape 2 collapsed to linear via memoization. The bridge to chapter 9.0.
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Tree recursion + memo: each subproblem computed once, total Theta(n)."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# Shape 3: divide-and-conquer. Split, recurse on halves, combine.
# T(n) = 2T(n/2) + Theta(n) -> Theta(n log n) by master theorem case 2.
def merge_sort(nums: List[int]) -> List[int]:
    """Divide-and-conquer sort: split in half, recurse, merge."""
    if len(nums) <= 1:
        return nums[:]
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    out: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out


# Canonical chapter entrypoint.
def fib(n: int) -> int:
    return fib_memo(n)
