# LC 174. Dungeon Game
# Recurrence:
#   dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
# Sentinel base cells dp[m][n-1] = dp[m-1][n] = 1 enforce "knight must
# arrive with at least 1 HP". Iteration is bottom-right to top-left.
"""Backward grid DP: minimum starting HP for a knight to reach the princess.

Forward DP fails because the survival predicate "HP >= 1 at every cell"
depends on the suffix of the path, not the prefix. Iterating from
(m-1, n-1) back to (0, 0) lets each cell read its already-computed
successors and take the cheaper one.
"""

from typing import List


def calculate_minimum_hp(dungeon: List[List[int]]) -> int:
    m = len(dungeon)
    n = len(dungeon[0])
    # dp[i][j] = minimum HP required ON ENTERING (i, j) to survive the path.
    # Pad with sentinel inf so the (m-1, n-1) cell reads min(inf, inf) and
    # falls back to its own clamp.
    INF = float("inf")
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    dp[m][n - 1] = 1
    dp[m - 1][n] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(need, 1)
    return dp[0][0]
