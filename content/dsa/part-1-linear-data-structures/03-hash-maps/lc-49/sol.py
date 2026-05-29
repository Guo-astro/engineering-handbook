# LC 49. Group Anagrams
# Bucket by canonical form. The 26-int character-count tuple is O(k) per
# string vs O(k log k) for sorted-string keys, where k is string length.
# defaultdict(list) handles the "create-then-append" idiom in one line.
# O(N * k) time, O(N * k) space, for N strings of average length k.
from typing import Dict, List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups: Dict[tuple, List[str]] = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(s)
    return list(groups.values())
