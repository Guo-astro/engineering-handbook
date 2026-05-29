# LC 518. Coin Change II
# OUTER loop = coins is mandatory; counts unordered combinations.
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1                           # empty multiset is one valid way
    for c in coins:                     # OUTER = coins -> combinations
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
