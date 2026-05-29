# LC 51. N-Queens (and LC 52. N-Queens II as the count-only sibling)
# (counts: 1, 2, 92, 724 -- matches OEIS A000170).
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """LC 51 -- return all distinct n-queens boards as char arrays."""
    solutions: List[List[str]] = []
    queens = [-1] * n

    def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
        if row == n:
            solutions.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in queens])
            return
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        while available:
            bit = available & -available             # isolate lowest set bit
            col = bit.bit_length() - 1
            queens[row] = col
            backtrack(row + 1,
                      cols | bit,
                      (diag1 | bit) << 1,
                      (diag2 | bit) >> 1)
            available &= available - 1               # try the next column

    backtrack(0, 0, 0, 0)
    return solutions


def total_n_queens(n: int) -> int:
    """LC 52 -- count-only variant; same recursion, no board built."""
    count = 0

    def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        while available:
            bit = available & -available
            backtrack(row + 1,
                      cols | bit,
                      (diag1 | bit) << 1,
                      (diag2 | bit) >> 1)
            available &= available - 1

    backtrack(0, 0, 0, 0)
    return count
