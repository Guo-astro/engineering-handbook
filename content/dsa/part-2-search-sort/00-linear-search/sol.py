"""LC linear search — scan an unsorted sequence, return first match index.

The contract: walk the array left to right, return the index of the first
element equal to target, or -1 if none. This is Knuth Algorithm B from
The Art of Computer Programming Volume 3 §6.1, the foundation every other
search algorithm in this part is measured against.
"""
from typing import List


def linear_search(nums: List[int], target: int) -> int:
    """Scan left-to-right; return first index where nums[i] == target, else -1.

    Loop invariant (CLRS Exercise 2.1-3): at the start of each iteration,
    nums[0..i-1] does not contain target. Initialisation holds vacuously.
    Maintenance holds because either nums[i] == target and the loop returns,
    or nums[i] != target and the invariant extends to nums[0..i].
    Termination at i == len(nums) says no index in nums[0..n-1] matches.
    """
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
