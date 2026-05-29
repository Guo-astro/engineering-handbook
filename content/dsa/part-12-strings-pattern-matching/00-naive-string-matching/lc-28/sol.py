# LC 28. Find the Index of the First Occurrence in a String
def str_str(haystack: str, needle: str) -> int:
    """Return the first index where needle occurs in haystack, or -1."""
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1
        if j == m:
            return i
    return -1
