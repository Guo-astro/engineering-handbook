# LC 416. Partition Equal Subset Sum
from typing import List


def can_partition(nums: List[int]) -> bool:
    """LC 416: can nums be split into two equal-sum subsets?"""
    total = sum(nums)
    if total & 1:
        return False
    target = total // 2

    # dp[j] is True iff some subset of seen items sums exactly to j.
    dp = [False] * (target + 1)
    dp[0] = True  # empty subset sums to 0

    for x in nums:
        # Iterate capacity right-to-left so each item contributes at most once.
        # Going left-to-right would reuse x in the same pass and break 0/1.
        for j in range(target, x - 1, -1):
            dp[j] = dp[j] or dp[j - x]
        if dp[target]:
            return True
    return dp[target]
