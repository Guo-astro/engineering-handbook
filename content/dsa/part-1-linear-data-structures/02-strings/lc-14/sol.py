# LC 14. Longest Common Prefix
# Vertical scanning: walk columns of the shortest string; on first mismatch,
# return the prefix up to that column. Early-exit beats horizontal reduce on
# inputs that diverge near the front. O(S) where S = sum of lengths, O(1).
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for s in strs:
            if s[i] != ch:
                return shortest[:i]
    return shortest
