# LC 213. House Robber II
from typing import List


def rob(nums: List[int]) -> int:
    """LC 213 House Robber II. Circular -> two linear sub-passes, max of both."""
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    # skip last, then skip first; the circular adjacency is broken in each pass
    return max(_rob_linear(nums[:-1]), _rob_linear(nums[1:]))


def _rob_linear(houses: List[int]) -> int:
    """Linear House Robber I via rolling-pair tabulation, O(1) space.

    Recurrence: dp[i] = max(dp[i-1], dp[i-2] + houses[i]).
    Only the last two values matter, so carry (prev2, prev1).
    """
    prev2, prev1 = 0, 0
    for x in houses:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
