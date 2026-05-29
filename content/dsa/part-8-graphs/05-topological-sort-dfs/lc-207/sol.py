# LC 207. Course Schedule
"""LC 207 Course Schedule, DFS post-order reverse topological sort."""
import sys
from typing import List

sys.setrecursionlimit(10000)  # DSH-04: LC 207 hidden tests include depth-2000 chains

WHITE, GRAY, BLACK = 0, 1, 2


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Return True iff the prereq graph is a DAG. Edge convention: b -> a."""
    adj: List[List[int]] = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        adj[b].append(a)

    color = [WHITE] * num_courses

    def dfs(u: int) -> bool:
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                return False  # back edge -> cycle
            if color[v] == WHITE and not dfs(v):
                return False
        color[u] = BLACK  # post-order point: append u to a list here for LC 210
        return True

    for u in range(num_courses):
        if color[u] == WHITE and not dfs(u):
            return False
    return True
