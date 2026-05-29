# LC 322. Coin Change
# [1,2,5]/11=3, [2]/3=-1, [1]/0=0 all PASS.
from typing import List

INF = float('inf')


def coin_change(coins: List[int], amount: int) -> int:
    """Minimum number of coins summing to `amount`, or -1 if not reachable.
    Each coin may be reused unlimited times.
    """
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1
