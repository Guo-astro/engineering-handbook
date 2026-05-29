# LC 91. Decode Ways


def num_decodings(s: str) -> int:
    """LC 91 Decode Ways. Return the number of ways to decode digit string s.

    dp[i] = number of decodings of the prefix s[:i].
    Rolling-window: only prev2 = dp[i-2] and prev1 = dp[i-1] live across iters.
    """
    n = len(s)
    if n == 0 or s[0] == "0":
        return 0
    prev2, prev1 = 1, 1
    for i in range(2, n + 1):
        cur = 0
        # Single-digit decode: s[i-1] in '1'..'9'.
        if s[i - 1] != "0":
            cur += prev1
        # Two-digit decode: s[i-2:i] in '10'..'26'.
        two = int(s[i - 2 : i])
        if 10 <= two <= 26:
            cur += prev2
        prev2, prev1 = prev1, cur
    return prev1
