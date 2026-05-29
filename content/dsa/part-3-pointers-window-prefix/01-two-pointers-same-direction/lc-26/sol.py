# LC 26. Remove Duplicates from Sorted Array
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """LC 26: Remove duplicates from a sorted array in-place; return new length k.

    Invariant: at any moment, nums[0..write) is a sorted prefix of distinct
    elements drawn from the values seen so far. Each new element either
    extends the prefix (if it differs from nums[write - 1]) or is dropped.
    """
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
