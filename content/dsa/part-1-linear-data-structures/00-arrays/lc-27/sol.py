# LC 27. Remove Element
# Two-pointer compaction: read pointer i scans every slot, write pointer k
# advances only on keepers. Returns the new logical length. O(n), O(1).
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
