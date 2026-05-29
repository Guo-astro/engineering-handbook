# LC 78. Subsets
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """LC 78. Return every subset via DFS with start index."""
    result: List[List[int]] = []
    path: List[int] = []

    def dfs(start: int) -> None:
        result.append(path.copy())   # snapshot at every node
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)               # i+1 prevents reuse and reordering
            path.pop()               # undo for backtrack

    dfs(0)
    return result
