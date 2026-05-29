# LC 1044. Longest Duplicate Substring
# Note: this chapter ships LC 1044 in Python only (reference: Python only).
from typing import Optional


def longest_dup_substring(s: str) -> str:
    """LC 1044. Find any longest substring that appears at least twice.

    Binary-search the answer length L in [1, n - 1]. At each L, run a
    Rabin-Karp scan over s using a precomputed prefix-hash array;
    insert each window's hash into a dict keyed by hash, value = first
    starting index. On collision (same hash already present) verify
    by string slice; if equal, L is feasible. The binary search is
    monotone because a duplicate of length L+1 contains a duplicate of
    length L.
    """
    n = len(s)
    if n < 2:
        return ""

    # Precompute prefix hashes over s with the same (base, mod) used in
    # the chapter's str_str. h[i] = hash(s[0..i-1]); pow_b[i] = base^i.
    base = 256
    mod = (1 << 61) - 1                # 2^61 - 1, a Mersenne prime
    h = [0] * (n + 1)
    pow_b = [1] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * base + ord(s[i])) % mod
        pow_b[i + 1] = (pow_b[i] * base) % mod

    def window_hash(left: int, length: int) -> int:
        # hash(s[left..left+length-1]) via prefix-hash subtraction.
        return (h[left + length] - h[left] * pow_b[length]) % mod

    def find_dup(length: int) -> Optional[int]:
        seen: dict[int, list[int]] = {}
        for i in range(n - length + 1):
            wh = window_hash(i, length)
            if wh in seen:
                for j in seen[wh]:
                    if s[j:j + length] == s[i:i + length]:   # verify
                        return j
                seen[wh].append(i)
            else:
                seen[wh] = [i]
        return None

    lo, hi = 1, n - 1
    best_start, best_len = 0, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        start = find_dup(mid)
        if start is not None:
            best_start, best_len = start, mid
            lo = mid + 1
        else:
            hi = mid - 1

    return s[best_start:best_start + best_len]
