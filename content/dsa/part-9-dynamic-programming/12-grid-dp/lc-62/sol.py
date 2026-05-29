# LC 62. Unique Paths
"""Forward grid DP: count monotone right/down paths from (0, 0) to (m-1, n-1).

The recurrence is the unweighted count `dp[i][j] = dp[i-1][j] + dp[i][j-1]`,
filled row-major top-to-bottom, left-to-right. Two implementations: the
full 2D table for clarity, and the rolling 1D row for `O(min(m, n))` space.
"""

from typing import List


def unique_paths_2d(m: int, n: int) -> int:
    """Full 2D table DP. dp[i][j] = dp[i-1][j] + dp[i][j-1]."""
    dp = [[0] * n for _ in range(m)]
    for j in range(n):
        dp[0][j] = 1
    for i in range(m):
        dp[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


def unique_paths_1d(m: int, n: int) -> int:
    """Rolling 1D row. O(m*n) time, O(min(m, n)) space."""
    if m < n:
        m, n = n, m
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]
    return dp[n - 1]


def unique_paths(m: int, n: int) -> int:
    """LeetCode-shaped entry point. Defaults to the full 2D table."""
    return unique_paths_2d(m, n)
