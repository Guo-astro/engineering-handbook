# LC 84. Largest Rectangle in Histogram
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    """LC 84. Returns max rectangle area in histogram."""
    ans = 0
    stack: List[int] = []  # non-decreasing stack of indices
    n = len(heights)
    for i in range(n + 1):
        cur = 0 if i == n else heights[i]
        while stack and heights[stack[-1]] > cur:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            if h * w > ans:
                ans = h * w
        stack.append(i)
    return ans
