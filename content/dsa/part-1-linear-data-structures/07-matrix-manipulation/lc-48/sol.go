// LC 48. Rotate Image
// Rotate an n x n matrix 90 degrees clockwise in place via two passes:
// transpose along the main diagonal, then reverse each row. The transpose
// inner loop must start at j = i + 1 or each off-diagonal pair gets
// swapped twice, returning the matrix to its original state.
// O(n^2) time, O(1) space.
package main

func rotate(matrix [][]int) {
	n := len(matrix)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
	for _, row := range matrix {
		for l, r := 0, n-1; l < r; l, r = l+1, r-1 {
			row[l], row[r] = row[r], row[l]
		}
	}
}
