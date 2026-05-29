# LC 200. Number of Islands
from collections import deque
from typing import List
import sys

# 300x300 grid is the LC 200 constraint upper bound; recursive DFS on an
# all-ones grid recurses ~90,000 deep. Python's default recursion limit
# is ~1000, so iterative BFS is the safe default. Raise the limit only
# if you must use recursive DFS.
sys.setrecursionlimit(10**6)


def num_islands(grid: List[List[str]]) -> int:
    """LC 200. Count maximal 4-connected components of '1' in the grid.

    Outer scan visits every cell once. When it lands on an unvisited '1',
    increment the component counter and run BFS to mark every reachable
    land cell as water. The outer scan is the algorithm; BFS is the engine.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(sr: int, sc: int) -> None:
        q = deque([(sr, sc)])
        grid[sr][sc] = "0"          # mark visited at enqueue, not dequeue
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    q.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                bfs(r, c)
    return count
