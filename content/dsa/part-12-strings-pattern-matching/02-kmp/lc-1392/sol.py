# LC 1392. Longest Happy Prefix
# The compute_lps subroutine is the
# verified version; a "happy prefix" is the longest proper
# prefix that is also a suffix, which is literally s[:lps[n-1]].
def compute_lps(pattern: str) -> list[int]:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def longest_prefix(s: str) -> str:
    """Return the longest non-empty proper prefix of s that is also a suffix.
    The entire problem is one application of the LPS construction.
    Time O(n), space O(n)."""
    n = len(s)
    if n < 2:
        return ""
    lps = compute_lps(s)
    return s[:lps[n - 1]]
