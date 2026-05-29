# LC 1368. Minimum Cost to Make at Least One Valid Path in a Grid
from collections import deque
from typing import List


def min_cost_grid_01_bfs(grid: List[List[int]]) -> int:
    """LC 1368. 0-1 BFS: free moves push-front, cost-1 moves push-back."""
    rows, cols = len(grid), len(grid[0])
    DIRS = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}   # LC's encoding

    INF = float("inf")
    dist = [[INF] * cols for _ in range(rows)]
    dist[0][0] = 0

    dq = deque([(0, 0)])
    while dq:
        r, c = dq.popleft()
        for d, (dr, dc) in DIRS.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cost = 0 if grid[r][c] == d else 1
                nd = dist[r][c] + cost
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))
    return dist[rows - 1][cols - 1]
