# LC 130. Surrounded Regions
import sys
sys.setrecursionlimit(10**6)  # DSH-04: deep grids approach n*m recursion depth.


def solve(board: list[list[str]]) -> None:
    """LC 130 Surrounded Regions: capture every 'O' region not touching the border."""
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        # Bounds + only walk live 'O' cells.
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O":
            return
        board[r][c] = "#"  # mark border-connected
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Sweep the four borders, DFS from any 'O' we find.
    for r in range(m):
        dfs(r, 0)
        dfs(r, n - 1)
    for c in range(n):
        dfs(0, c)
        dfs(m - 1, c)

    # Final sweep: '#' was border-connected (restore), 'O' was surrounded (capture).
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "#":
                board[r][c] = "O"
