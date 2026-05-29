# LC 15. 3Sum
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """LC 15: return every unique triplet of values summing to zero.

    Sort, then for each anchor i run a converging two-pointer sweep over the
    suffix targeting -nums[i]. Three duplicate-skip lines do all the work:
    skip equal anchors, and after each hit advance both pointers past their
    own value runs. O(n^2) time, O(1) auxiliary space (sort excluded).
    """
    nums = sorted(nums)
    n = len(nums)
    out: List[List[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return out
