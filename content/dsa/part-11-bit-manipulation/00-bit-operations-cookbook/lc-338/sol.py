# LC 338. Counting Bits


def count_bits(n: int) -> list[int]:
    """Return ans[i] = popcount(i) for i in 0..n.

    Recurrence: dp[i] = dp[i & (i - 1)] + 1.
    Cleared-lowest-bit subproblem already solved; add one for the bit just removed.
    O(n) time, O(n) space (output dominates).
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
