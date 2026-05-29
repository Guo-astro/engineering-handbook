# LC 46. Permutations
# mechanism pseudocode and §5.3.
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """LC 46. Return every permutation via DFS with a used[] mask."""
    result: List[List[int]] = []
    path: List[int] = []
    used: List[bool] = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            result.append(path.copy())   # snapshot only at full-length leaves
            return
        for i in range(len(nums)):
            if used[i]:
                continue                 # element already in path; skip
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()                   # undo for backtrack
            used[i] = False

    dfs()
    return result
