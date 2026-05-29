# LC 72. Edit Distance

def min_distance(word1: str, word2: str) -> int:
    """LC 72: minimum number of operations to convert word1 to word2."""
    m, n = len(word1), len(word2)
    # dp[i][j] = edit distance between word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i  # i deletes turn word1[:i] into ""
    for j in range(n + 1):
        dp[0][j] = j  # j inserts turn "" into word2[:j]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]               # match: free diagonal
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],                     # replace
                    dp[i - 1][j],                         # delete from word1
                    dp[i][j - 1],                         # insert into word1
                )
    return dp[m][n]


def min_distance_rolling(word1: str, word2: str) -> int:
    """O(min(m, n)) space variant using two rolling rows."""
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j - 1], prev[j], curr[j - 1])
        prev, curr = curr, prev
    return prev[n]
