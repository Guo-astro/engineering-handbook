# LC 28. Find the Index of the First Occurrence in a String


def str_str(haystack: str, needle: str) -> int:
    """LC 28. First index of needle in haystack via Rabin-Karp, or -1.

    Slide a length-m window across the haystack; compare each window's
    polynomial hash against the precomputed needle hash; on hash match,
    verify char-by-char to defeat collisions. Expected O(n + m); worst
    case O(n * m) when every window collides.
    """
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    if m > n:
        return -1

    base = 256
    mod = 1_000_000_007
    high_power = pow(base, m - 1, mod)

    needle_hash = 0
    window_hash = 0
    for i in range(m):
        needle_hash = (needle_hash * base + ord(needle[i])) % mod
        window_hash = (window_hash * base + ord(haystack[i])) % mod

    for i in range(n - m + 1):
        if window_hash == needle_hash:
            if haystack[i:i + m] == needle:        # verify on hash match
                return i
        if i < n - m:
            leading = ord(haystack[i]) * high_power
            window_hash = (window_hash - leading) % mod
            window_hash = (window_hash * base + ord(haystack[i + m])) % mod

    return -1
