# LC 785. Is Graph Bipartite?
from collections import deque
from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    """LC 785 — true iff `graph` admits a 2-coloring (no odd cycle)."""
    n = len(graph)
    color = [0] * n                       # 0 = unvisited, 1 / -1 = the two color classes
    for start in range(n):
        if color[start] != 0:
            continue                      # already painted by a prior component
        color[start] = 1
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = -color[u]  # flip color across the edge
                    q.append(v)
                elif color[v] == color[u]:
                    return False          # same-color edge: odd cycle
    return True
