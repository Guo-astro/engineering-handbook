# LC 300. Longest Increasing Subsequence
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """LC 300 Longest Increasing Subsequence: O(n^2) DP.

    dp[i] = length of the longest STRICTLY increasing subsequence
    ending exactly at index i (and including nums[i]).
    """
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)
