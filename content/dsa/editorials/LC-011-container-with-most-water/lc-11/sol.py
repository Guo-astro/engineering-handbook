# LC 11. Container With Most Water
from typing import List


def max_area(height: List[int]) -> int:
    """LC 11: maximum water held between two walls in `height`.

    Two pointers, opposite ends. At each step, compute the candidate area
    `min(h[l], h[r]) * (r - l)`, then advance the pointer at the strictly
    shorter wall (ties: advance the right pointer, by convention). The
    case-analysis proof is in the editorial: advancing the taller wall
    cannot improve the answer because the shorter wall still binds and
    the width strictly shrinks. O(n) time, O(1) space.
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h_l, h_r = height[left], height[right]
        width = right - left
        if h_l < h_r:
            area = h_l * width
            if area > best:
                best = area
            left += 1
        else:
            area = h_r * width
            if area > best:
                best = area
            right -= 1
    return best
