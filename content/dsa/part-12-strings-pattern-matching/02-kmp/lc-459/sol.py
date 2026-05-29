# LC 459. Repeated Substring Pattern
# The compute_lps subroutine is the
# verified version; the closed-form check
# `n % (n - lps[n-1]) == 0` is the canonical KMP-trick proof from
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


def repeated_substring_pattern(s: str) -> bool:
    """A string s is the concatenation of k>=2 copies of a smaller substring
    iff lps[n-1] != 0 AND n is divisible by (n - lps[n-1]).
    Time O(n), space O(n)."""
    n = len(s)
    if n < 2:
        return False
    lps = compute_lps(s)
    period = n - lps[n - 1]
    # period < n is guaranteed because lps records the longest PROPER
    # prefix-suffix; the divisibility test rules out partial matches.
    return lps[n - 1] != 0 and n % period == 0
