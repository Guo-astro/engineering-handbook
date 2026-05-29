# LC 547. Number of Provinces
from collections import deque
from typing import List


def find_circle_num(is_connected: List[List[int]]) -> int:
    """LC 547. Count connected components of an undirected graph
    given as an n-by-n adjacency matrix.

    Same outer-scan-and-flood template as LC 200; only the neighbor
    function changes. For city i, neighbors are j where
    is_connected[i][j] == 1 and j != i.
    """
    n = len(is_connected)
    visited = [False] * n
    count = 0

    def bfs(start: int) -> None:
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            for v in range(n):
                if is_connected[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    q.append(v)

    for i in range(n):
        if not visited[i]:
            count += 1
            bfs(i)
    return count
