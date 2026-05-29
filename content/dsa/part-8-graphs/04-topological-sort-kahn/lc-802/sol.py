# LC 802. Find Eventual Safe States
"""LC 802 Find Eventual Safe States — reverse-graph Kahn."""
from collections import deque
from typing import List


def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    """Return all vertices from which every path terminates (no cycle reachable).

    Insight: a vertex is safe iff in the *reversed* graph it can be emitted
    by Kahn starting from terminal vertices (out-degree zero in the original,
    indegree zero after reversal). Reverse all edges, seed Kahn from
    original-terminal vertices, return the emitted set sorted.
    """
    n = len(graph)
    rev_indeg = [0] * n          # = original out-degree
    rev_adj: List[List[int]] = [[] for _ in range(n)]
    for u, succs in enumerate(graph):
        for v in succs:
            rev_adj[v].append(u)  # reverse edge: v -> u
            rev_indeg[u] += 1     # u's reversed indegree = u's original out-degree

    q = deque(v for v in range(n) if rev_indeg[v] == 0)
    safe = [False] * n
    while q:
        u = q.popleft()
        safe[u] = True
        for v in rev_adj[u]:
            rev_indeg[v] -= 1
            if rev_indeg[v] == 0:
                q.append(v)
    return [v for v in range(n) if safe[v]]
