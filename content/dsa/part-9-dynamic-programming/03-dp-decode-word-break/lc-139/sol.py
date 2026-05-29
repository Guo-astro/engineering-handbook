# LC 139. Word Break


def word_break(s: str, word_dict: list[str]) -> bool:
    """LC 139 Word Break. Bottom-up O(n * L_max).

    dp[i] = True iff some j < i has dp[j] True AND s[j:i] is in the dict.
    The L_max bound on the inner loop cuts O(n^2) -> O(n * L_max).
    """
    n = len(s)
    words = set(word_dict)
    max_w = max((len(w) for w in words), default=0)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        lo = max(0, i - max_w)
        for j in range(lo, i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
