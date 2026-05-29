// LC 54. Spiral Matrix
// Walk an m x n matrix in clockwise spiral order using four shrinking
// boundaries. The two `if top <= bottom` and `if left <= right` guards
// inside the loop are mandatory: without them, odd-shaped rectangles
// re-emit the bottom row or right column. Square matrices accidentally
// work without the guards, hiding the bug. O(m*n), O(1) extra.
package main

func spiralOrder(matrix [][]int) []int {
	out := []int{}
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return out
	}
	top, bottom := 0, len(matrix)-1
	left, right := 0, len(matrix[0])-1
	for top <= bottom && left <= right {
		for j := left; j <= right; j++ {
			out = append(out, matrix[top][j])
		}
		top++
		for i := top; i <= bottom; i++ {
			out = append(out, matrix[i][right])
		}
		right--
		if top <= bottom {
			for j := right; j >= left; j-- {
				out = append(out, matrix[bottom][j])
			}
			bottom--
		}
		if left <= right {
			for i := bottom; i >= top; i-- {
				out = append(out, matrix[i][left])
			}
			left++
		}
	}
	return out
}
