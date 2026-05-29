# LC 54. Spiral Matrix
# Walk an m x n matrix in clockwise spiral order using four shrinking
# boundaries. The two `if top <= bottom` and `if left <= right` guards
# inside the loop are mandatory: without them, odd-shaped rectangles
# re-emit the bottom row or right column. Square matrices accidentally
# work without the guards, hiding the bug. O(m*n), O(1) extra.
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    out: List[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            out.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            out.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                out.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                out.append(matrix[i][left])
            left += 1
    return out
