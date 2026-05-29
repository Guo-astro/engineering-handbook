# LC 1143. Longest Common Subsequence
#           (("abcde","ace")=3, ("abc","abc")=3, ("abc","def")=0,
#            ("ABCBDAB","BDCAB")=4, ("","abc")=0, ("a","a")=1).
def longest_common_subsequence(text1: str, text2: str) -> int:
    """LC 1143: length of the longest common subsequence.

    Bottom-up tabulation per CLRS 14.4. dp[i][j] holds the LCS length of
    text1[:i] vs text2[:j]. Row 0 and column 0 are zero (empty prefix).
    O(m*n) time, O(m*n) space.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lcs_with_reconstruction(text1: str, text2: str) -> tuple[int, str]:
    """Recover an actual LCS string by backtracking from (m, n) per CLRS PRINT-LCS.

    Requires the full 2D table (the rolling-row optimization loses the
    parent pointers the backtrack needs). Backtrack runs in O(m + n).
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    out = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            out.append(text1[i - 1])
            i, j = i - 1, j - 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    out.reverse()
    return dp[m][n], "".join(out)


def longest_common_subsequence_rolling(text1: str, text2: str) -> int:
    """Length-only variant in O(min(m, n)) space.

    Iterate the shorter string along the inner dimension so the rolling
    row is as small as possible. The diagonal predecessor (dp[i-1][j-1])
    must be saved into a scalar before being overwritten by the next
    write to the previous row.
    """
    if len(text1) < len(text2):
        text1, text2 = text2, text1  # iterate the shorter as the inner axis
    n = len(text2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    for i in range(1, len(text1) + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev  # swap; reusing the old prev as next row's scratch
        for k in range(n + 1):
            curr[k] = 0  # zero-out the row we're about to fill
    return prev[n]
