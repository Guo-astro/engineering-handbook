# LC 847. Shortest Path Visiting All Nodes
# Bitmask BFS over (node, mask) states. State count n * 2^n; transitions
# enumerate node neighbors. O(n^2 * 2^n) time, O(n * 2^n) space. n <= 12
# per LC constraints.
from collections import deque
from typing import List


def shortest_path_length(graph: List[List[int]]) -> int:
    """LC 847. Shortest path that visits every node (revisits allowed)."""
    n = len(graph)
    if n == 1:
        return 0
    full_mask = (1 << n) - 1

    # Visited table indexed by (node, mask). True the first time the BFS
    # reaches that state, which is the shortest distance to it.
    visited = [[False] * (1 << n) for _ in range(n)]
    queue = deque()
    for i in range(n):
        start_mask = 1 << i
        visited[i][start_mask] = True
        queue.append((i, start_mask, 0))

    while queue:
        node, mask, dist = queue.popleft()
        if mask == full_mask:
            return dist
        for nb in graph[node]:
            new_mask = mask | (1 << nb)
            if not visited[nb][new_mask]:
                visited[nb][new_mask] = True
                queue.append((nb, new_mask, dist + 1))

    return -1  # LC constraints guarantee connectivity; defensive.
