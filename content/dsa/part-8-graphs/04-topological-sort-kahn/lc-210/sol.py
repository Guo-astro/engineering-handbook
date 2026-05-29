# LC 210. Course Schedule II
"""LC 210 Course Schedule II — Kahn's algorithm; emit the order itself."""
from collections import deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return any valid course ordering, or [] if a cycle exists.

    Edge convention: prerequisites[i] = [a, b] means b must be taken before a,
    so the directed edge is b -> a. Same Kahn machinery as LC 207; instead of
    counting visited vertices we append them to the order list and return it
    when its length equals num_courses.
    """
    indeg = [0] * num_courses
    adj: List[List[int]] = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    q = deque(v for v in range(num_courses) if indeg[v] == 0)
    order: List[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_courses else []
