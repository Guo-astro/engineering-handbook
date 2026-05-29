# LC 79. Word Search
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """LC 79 Word Search: does `word` exist as a path of 4-adjacent cells on `board`?"""
    if not board or not board[0] or not word:
        return False
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, k: int) -> bool:
        if k == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
            return False
        saved = board[r][c]
        board[r][c] = "#"   # in-place visited marker; sentinel never matches a word char
        found = (dfs(r + 1, c, k + 1) or
                 dfs(r - 1, c, k + 1) or
                 dfs(r, c + 1, k + 1) or
                 dfs(r, c - 1, k + 1))
        board[r][c] = saved  # restore on backtrack
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False
