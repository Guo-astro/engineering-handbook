# LC 303. Range Sum Query - Immutable
from typing import List


class NumArray:
    """LC 303. Construct in O(n); answer sumRange in O(1).

    Invariant: prefix[i] = nums[0] + nums[1] + ... + nums[i-1] for i in [0, n].
    Range sum nums[l..r] inclusive = prefix[r+1] - prefix[l].
    """

    def __init__(self, nums: List[int]) -> None:
        n = len(nums)
        # prefix has length n + 1; prefix[0] = 0 is the empty-sum sentinel.
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
