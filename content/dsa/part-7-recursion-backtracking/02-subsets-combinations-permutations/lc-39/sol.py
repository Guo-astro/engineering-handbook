# LC 39. Combination Sum
# mechanism (recurse with i, not i+1, to allow reuse).
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """LC 39. Return every combination of candidates summing to target. Reuse allowed."""
    result: List[List[int]] = []
    path: List[int] = []
    candidates.sort()                           # sort enables the early break below

    def dfs(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path.copy())          # snapshot when target hit exactly
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break                           # sorted: no later candidate fits either
            path.append(candidates[i])
            dfs(i, remaining - candidates[i])   # i, not i+1 — reuse same element
            path.pop()                          # undo for backtrack

    dfs(0, target)
    return result
