# LC 128. Longest Consecutive Sequence
# Build a hash set, then for each value, only start an inner walk when
# (x - 1) is absent — i.e., x is the minimum of its run. Each element is
# touched at most twice, giving O(n) total work assuming O(1) average
# set membership. O(n) time, O(n) space.
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    s = set(nums)
    best = 0
    for x in s:
        if (x - 1) not in s:
            y = x + 1
            while y in s:
                y += 1
            best = max(best, y - x)
    return best
