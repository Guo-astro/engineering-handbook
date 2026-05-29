# LC 1. Two Sum
from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    """LC 1: return indices of two numbers in nums summing to target.

    One pass with a value -> first-seen-index map. For each x, look up the
    complement (target - x) BEFORE inserting x; the lookup-then-insert order
    is what prevents matching an element against itself on inputs like [3, 3].
    O(n) average time, O(n) space.
    """
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
