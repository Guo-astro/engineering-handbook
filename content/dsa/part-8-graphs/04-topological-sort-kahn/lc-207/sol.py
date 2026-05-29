# LC 207. Course Schedule
"""LC 207 Course Schedule — Kahn's algorithm reference."""
from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Return True iff all courses can be finished (the prereq graph is a DAG).

    Edge convention: prerequisites[i] = [a, b] means b must be taken before a,
    so the directed edge is b -> a in the dependency graph. Run a Kahn
    topological sort on (V, E) and report True iff we order all V vertices.
    """
    indeg = [0] * num_courses
    adj: List[List[int]] = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    q = deque(v for v in range(num_courses) if indeg[v] == 0)
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return visited == num_courses
