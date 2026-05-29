# LC 242. Valid Anagram
# Increment-decrement-and-check: build a counter from s, then walk t
# decrementing; any underflow means t is not a permutation of s.
# Length short-circuit avoids building the counter when sizes differ.
# O(n), O(k) where k is the alphabet size.
from typing import Dict


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: Dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True
