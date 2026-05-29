# DynArr — geometric-resize dynamic array reference template.
# Parameterized growth factor (growth_num / growth_den) for studying the
# amortized-O(1) push proof; tracks reallocation count to make the
# geometric pattern observable. Not an LC problem.
from __future__ import annotations
from typing import Any, Optional


class DynArr:
    def __init__(self, initial_cap: int = 1, growth_num: int = 2, growth_den: int = 1) -> None:
        if initial_cap < 1:
            raise ValueError("initial_cap must be >= 1")
        if growth_num <= growth_den:
            raise ValueError("growth_num must be > growth_den (factor > 1)")
        self._cap: int = initial_cap
        self._size: int = 0
        self._growth_num: int = growth_num
        self._growth_den: int = growth_den
        self._buf: list[Optional[Any]] = [None] * initial_cap
        self._reallocs: int = 0

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._cap

    def reallocations(self) -> int:
        return self._reallocs

    def get(self, i: int) -> Any:
        if i < 0 or i >= self._size:
            raise IndexError("get index out of range")
        return self._buf[i]

    def push(self, x: Any) -> None:
        if self._size == self._cap:
            self._grow()
        self._buf[self._size] = x
        self._size += 1

    def _grow(self) -> None:
        # Ceiling division so factors like 9/8 still grow on small caps.
        new_cap = (self._cap * self._growth_num + self._growth_den - 1) // self._growth_den
        # Guard against rounding to a no-op (would loop forever on next push).
        if new_cap <= self._cap:
            new_cap = self._cap + 1
        new_buf: list[Optional[Any]] = [None] * new_cap
        for i in range(self._size):
            new_buf[i] = self._buf[i]
        self._buf = new_buf
        self._cap = new_cap
        self._reallocs += 1


def simulate(initial_cap: int, growth_num: int, growth_den: int, n_push: int) -> tuple[int, int, int]:
    """Push n_push items into a fresh DynArr; return (size, capacity, reallocations)."""
    a = DynArr(initial_cap=initial_cap, growth_num=growth_num, growth_den=growth_den)
    for i in range(n_push):
        a.push(i)
    return a.size(), a.capacity(), a.reallocations()
