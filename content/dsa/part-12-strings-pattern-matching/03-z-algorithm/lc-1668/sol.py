# LC 1668. Maximum Repeating Substring
from typing import List


def z_function(s: str) -> List[int]:
    """Return the Z-array of s in O(n) time. z[0] = 0 by convention."""
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def max_repeating(sequence: str, word: str) -> int:
    """LC 1668: largest k such that word repeated k times is a substring of sequence."""
    m = len(word)
    if m == 0 or m > len(sequence):
        return 0
    s = word + "#" + sequence
    z = z_function(s)
    # Walk the Z-array over the text part, chaining matches at stride m.
    best = 0
    n = len(sequence)
    for start in range(n):
        i = m + 1 + start
        run = 0
        while i + m <= len(s) and z[i] >= m:
            run += 1
            i += m
        if run > best:
            best = run
    return best
