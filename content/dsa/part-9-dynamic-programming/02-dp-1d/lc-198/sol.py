# LC 198. House Robber
def rob(nums: list[int]) -> int:
    """LC 198 House Robber: max sum of non-adjacent elements.
    Two-options-per-cell DP: at each house, take + dp[i-2] OR skip = dp[i-1].
    O(n) time, O(1) space (rolling pair).
    """
    prev2, prev1 = 0, 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
