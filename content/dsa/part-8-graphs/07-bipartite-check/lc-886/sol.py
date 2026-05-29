# LC 886. Possible Bipartition
# Build adjacency from 1-indexed dislikes, then run the standard 2-coloring BFS.
from collections import deque
from typing import List


def possible_bipartition(n: int, dislikes: List[List[int]]) -> bool:
    """LC 886 — partition n people (1..n) into two groups such that no
    disliked pair lands in the same group. Equivalent to bipartite check
    on the dislikes graph.
    """
    graph = [[] for _ in range(n + 1)]      # index 0 unused; 1-indexed input
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (n + 1)                   # 0 = unvisited, 1 / -1 = two groups
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
