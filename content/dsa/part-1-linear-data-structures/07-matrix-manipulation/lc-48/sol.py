# LC 48. Rotate Image
# Rotate an n x n matrix 90 degrees clockwise in place via two passes:
# transpose along the main diagonal, then reverse each row. The transpose
# inner loop must start at j = i + 1 (not j = 0) or each off-diagonal
# pair gets swapped twice, returning the matrix to its original state.
# O(n^2) time, O(1) space.
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
