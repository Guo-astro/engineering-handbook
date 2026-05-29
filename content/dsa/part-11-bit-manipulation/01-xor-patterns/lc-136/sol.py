# LC 136. Single Number
from typing import List


def single_number(nums: List[int]) -> int:
    """LC 136 — element appearing once when every other element appears twice.
    O(n) time, O(1) space."""
    result = 0
    for x in nums:
        result ^= x
    return result
