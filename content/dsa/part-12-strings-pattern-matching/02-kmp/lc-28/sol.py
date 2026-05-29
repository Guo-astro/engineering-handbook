# LC 28. Find the Index of the First Occurrence in a String
def compute_lps(pattern: str) -> list[int]:
    """Failure function: lps[i] = length of the longest proper prefix
    of pattern[:i+1] that is also a suffix of pattern[:i+1]."""
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix-suffix
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]   # fall back; do NOT advance i
            else:
                lps[i] = 0
                i += 1
    return lps


def str_str(haystack: str, needle: str) -> int:
    """Return the index of the first occurrence of needle in haystack, or -1.
    Per LC 28, an empty needle returns 0. Time O(n+m), space O(m)."""
    if needle == "":
        return 0
    n, m = len(haystack), len(needle)
    if m > n:
        return -1
    lps = compute_lps(needle)
    i = 0  # haystack pointer
    j = 0  # needle pointer
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
