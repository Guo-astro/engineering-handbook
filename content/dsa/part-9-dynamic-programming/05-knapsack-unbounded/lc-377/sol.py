# LC 377. Combination Sum IV
# OUTER loop = amounts; counts ordered sequences (the problem statement
# explicitly says "different sequences are counted as different combinations").
from typing import List


def combination_sum4(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1                           # empty sequence is one valid way
    for a in range(1, target + 1):      # OUTER = amounts -> permutations
        for n in nums:
            if n <= a:
                dp[a] += dp[a - n]
    return dp[target]
