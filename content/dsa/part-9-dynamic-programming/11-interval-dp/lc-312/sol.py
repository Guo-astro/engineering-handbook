# LC 312. Burst Balloons
from typing import List


def max_coins(nums: List[int]) -> int:
    """LC 312. Interval DP with phantom 1s on both ends.

    dp[i][j] = max coins from bursting all balloons strictly between i and j
    on the padded array a = [1] + nums + [1]. The recurrence picks the LAST
    balloon to burst inside (i, j); when k is last, every other balloon in
    (i, k) and (k, j) has already gone, so k's neighbors at the moment it
    pops are exactly a[i] and a[j]. Length-major fill order keeps every
    smaller subproblem ready before the cell that needs it.
    """
    a = [1] + nums + [1]
    n = len(a)
    # Length < 2 means no balloons strictly inside (i, j); the zero default
    # is the correct base.
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length
            best = 0
            # k ranges over balloons strictly between i and j.
            for k in range(i + 1, j):
                gain = a[i] * a[k] * a[j] + dp[i][k] + dp[k][j]
                if gain > best:
                    best = gain
            dp[i][j] = best
    return dp[0][n - 1]
