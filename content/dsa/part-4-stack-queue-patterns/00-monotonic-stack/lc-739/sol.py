# LC 739. Daily Temperatures
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """LC 739. Returns days-until-warmer for each day; 0 if none."""
    n = len(temperatures)
    answer = [0] * n
    stack: List[int] = []  # decreasing stack of indices
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
