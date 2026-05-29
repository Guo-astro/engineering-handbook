# LC 37. Sudoku Solver
from typing import List


def box_index(r: int, c: int) -> int:
    """Map (row, col) to 3x3 box index 0..8 in row-major order."""
    return (r // 3) * 3 + (c // 3)


def solve_sudoku(board: List[List[str]]) -> None:
    """LC 37 Sudoku Solver, mutates board in place."""
    ALL = 0x1FF  # bits 0..8 -> digits 1..9 available
    rows = [ALL] * 9
    cols = [ALL] * 9
    boxes = [ALL] * 9

    for r in range(9):
        for c in range(9):
            ch = board[r][c]
            if ch != ".":
                bit = 1 << (int(ch) - 1)
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[box_index(r, c)] ^= bit

    def backtrack() -> bool:
        # MRV: scan empties, pick fewest-candidate cell.
        best = None
        best_count = 10
        best_mask = 0
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    continue
                cand = rows[r] & cols[c] & boxes[box_index(r, c)]
                count = bin(cand).count("1")
                if count < best_count:
                    best_count = count
                    best = (r, c)
                    best_mask = cand
                    if count <= 1:
                        break
            if best_count <= 1:
                break
        if best is None:
            return True            # no empties -> solved
        if best_count == 0:
            return False           # forward-check dead end

        r, c = best
        b = box_index(r, c)
        cand = best_mask
        while cand:
            bit = cand & -cand                # lowest set bit
            cand ^= bit
            d = bit.bit_length()              # 1..9
            board[r][c] = str(d)
            rows[r] ^= bit
            cols[c] ^= bit
            boxes[b] ^= bit
            if backtrack():
                return True
            rows[r] ^= bit
            cols[c] ^= bit
            boxes[b] ^= bit
            board[r][c] = "."
        return False

    backtrack()
