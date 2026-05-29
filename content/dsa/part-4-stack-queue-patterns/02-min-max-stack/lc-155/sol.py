# LC 155. Min Stack
#           duplicate-min probe, and all-same probe all pass.
from typing import List


class MinStack:
    """LC 155 Min Stack with O(1) push, pop, top, getMin via mirrored aux stack."""

    def __init__(self) -> None:
        self.values: List[int] = []
        self.mins: List[int] = []

    def push(self, val: int) -> None:
        self.values.append(val)
        # min(prev, val) preserves duplicate minima on the aux stack.
        # Strict `val < self.mins[-1]` is the canonical bug; see chapter pitfalls.
        current = val if not self.mins else min(self.mins[-1], val)
        self.mins.append(current)

    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]
