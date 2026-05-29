# LC 5. Longest Palindromic Substring
def longest_palindrome(s: str) -> str:
    """LC 5: 2D by-length DP. O(n^2) time, O(n^2) space."""
    n = len(s)
    if n == 0:
        return ""
    # is_palin[i][j] = True iff s[i..j] is a palindrome.
    is_palin = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # Base: every length-1 substring is a palindrome.
    for i in range(n):
        is_palin[i][i] = True

    # Length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palin[i][i + 1] = True
            start, max_len = i, 2

    # Length L from 3 to n, by-length fill.
    for L in range(3, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if s[i] == s[j] and is_palin[i + 1][j - 1]:
                is_palin[i][j] = True
                if L > max_len:
                    start, max_len = i, L

    return s[start:start + max_len]


def longest_palindrome_centers(s: str) -> str:
    """Same problem, expand-around-centers. O(n^2) time, O(1) space."""
    if not s:
        return ""

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # After the loop, [left+1, right-1] is the maximal palindrome.
        return left + 1, right - 1

    best_l, best_r = 0, 0
    for i in range(len(s)):
        # Odd-length palindrome centered at i.
        l1, r1 = expand(i, i)
        # Even-length palindrome centered between i and i+1.
        l2, r2 = expand(i, i + 1)
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
    return s[best_l:best_r + 1]
