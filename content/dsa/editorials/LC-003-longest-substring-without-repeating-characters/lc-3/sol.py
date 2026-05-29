# LC 3. Longest Substring Without Repeating Characters
from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """LC 3: length of the longest substring of s with no repeating characters.

    One pass with a last-index map. For each character at position r, if it
    was seen at index `prev` AND `prev >= l` (i.e., the prior occurrence is
    inside the current window), jump l to prev + 1 in O(1) instead of
    shrinking step by step. The `prev >= l` guard is mandatory: stale
    entries from before the current window must be ignored, otherwise l
    can move backwards into discarded territory.
    O(n) time, O(min(n, sigma)) space; under ASCII sigma=128, space is O(1).
    """
    last_index: Dict[str, int] = {}
    l = 0
    best = 0
    for r, c in enumerate(s):
        if c in last_index and last_index[c] >= l:
            l = last_index[c] + 1
        last_index[c] = r
        if r - l + 1 > best:
            best = r - l + 1
    return best
