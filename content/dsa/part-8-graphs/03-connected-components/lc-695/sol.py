# LC 695. Max Area of Island
from collections import deque
from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """LC 695. Return the area of the largest 4-connected island.

    Same outer scan as LC 200. The inner BFS now returns the number
    of land cells it visited so the outer scan can track a running max.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    best = 0

    def bfs(sr: int, sc: int) -> int:
        q = deque([(sr, sc)])
        grid[sr][sc] = 0
        size = 0
        while q:
            r, c = q.popleft()
            size += 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    q.append((nr, nc))
        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = bfs(r, c)
                if area > best:
                    best = area
    return best
