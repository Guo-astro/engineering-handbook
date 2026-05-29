# LC 307. Range Sum Query - Mutable
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def _build(self, nums: List[int], v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.tree[v] = nums[tl]
            return
        tm = (tl + tr) // 2
        self._build(nums, 2 * v, tl, tm)
        self._build(nums, 2 * v + 1, tm + 1, tr)
        self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def _update(self, v: int, tl: int, tr: int, pos: int, new_val: int) -> None:
        if tl == tr:
            self.tree[v] = new_val
            return
        tm = (tl + tr) // 2
        if pos <= tm:
            self._update(2 * v, tl, tm, pos, new_val)
        else:
            self._update(2 * v + 1, tm + 1, tr, pos, new_val)
        self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def sumRange(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return (self._query(2 * v, tl, tm, l, min(r, tm))
                + self._query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r))
