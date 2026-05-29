# LC 1971. Find if Path Exists in Graph
# Build an adjacency list from the edges, then BFS from source. The build
# is O(V + E); the BFS is O(V + E). Total O(V + E) time and space.
from collections import deque
from typing import List


def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)                       # undirected: push both halves
    visited = [False] * n
    visited[source] = True
    q = deque([source])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v == destination:
                return True
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return False
