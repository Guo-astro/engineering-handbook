# LC 55. Jump Game
# [(2,3,1,1,4)->True, (3,2,1,0,4)->False, [0]->True, [1]->True, [2,0,0]->True].
# Greedy max-reach frontier sweep. O(n) time, O(1) space.
from typing import List


def can_jump(nums: List[int]) -> bool:
    """LC 55. Can we reach the last index with the given jump-length budget?"""
    max_reach = 0
    n = len(nums)
    for i in range(n):
        if i > max_reach:
            return False
        if i + nums[i] > max_reach:
            max_reach = i + nums[i]
        if max_reach >= n - 1:
            return True
    return True
