# Suffix array via prefix doubling, plus Kasai LCP. O(n log^2 n) build, O(n) LCP.
from typing import List


def build_suffix_array(s: str) -> List[int]:
    """Suffix array of s via prefix doubling. O(n log^2 n) time."""
    n = len(s)
    if n == 0:
        return []
    sa = list(range(n))
    rank = [ord(c) for c in s]

    def key(i: int, k: int) -> tuple:
        return (rank[i], rank[i + k] if i + k < n else -1)

    k = 1
    while True:
        sa.sort(key=lambda i: key(i, k))
        tmp = [0] * n
        for j in range(1, n):
            same = key(sa[j], k) == key(sa[j - 1], k)
            tmp[sa[j]] = tmp[sa[j - 1]] + (0 if same else 1)
        rank = tmp
        if rank[sa[n - 1]] == n - 1:
            break
        k *= 2
    return sa


def build_lcp_kasai(s: str, sa: List[int]) -> List[int]:
    """Kasai O(n). lcp[i] = lcp(sa[i-1], sa[i]); lcp[0] = 0."""
    n = len(s)
    if n == 0:
        return []
    inv = [0] * n
    for i, p in enumerate(sa):
        inv[p] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if inv[i] > 0:
            j = sa[inv[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[inv[i]] = h
            if h > 0:
                h -= 1
    return lcp
