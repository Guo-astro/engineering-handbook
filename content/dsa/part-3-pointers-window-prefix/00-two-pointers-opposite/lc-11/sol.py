# LC 11. Container With Most Water
from typing import List


def max_area(height: List[int]) -> int:
    """LC 11 Container With Most Water."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h_l, h_r = height[left], height[right]
        if h_l < h_r:
            best = max(best, h_l * (right - left))
            left += 1
        else:
            best = max(best, h_r * (right - left))
            right -= 1
    return best
