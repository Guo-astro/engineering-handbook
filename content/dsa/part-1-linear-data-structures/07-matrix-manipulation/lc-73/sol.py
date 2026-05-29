# LC 73. Set Matrix Zeroes
# In place, O(1) extra space. Use row 0 and column 0 as the marker arrays;
# two booleans capture whether row 0 or column 0 originally contained a
# zero (the marker pass overwrites cell (0, 0) and loses that information).
# Read the flags BEFORE the marker pass — that ordering is the bug fix.
# O(m*n) time, O(1) extra space.
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
    # Pass 1: mark dirty rows and columns using the first row/col as flags.
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # Pass 2: apply marks to the inner region.
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # Pass 3: zero row 0 and column 0 themselves if they were originally dirty.
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
