// LC 51. N-Queens (and LC 52. N-Queens II as the count-only sibling)
// runtime tests pass for n in {1, 4, 8, 10}
// (counts: 1, 2, 92, 724 -- matches OEIS A000170).
package main

func SolveNQueens(n int) [][]string {
	out := [][]string{}
	queens := make([]int, n)
	var backtrack func(row, cols, diag1, diag2 int)
	backtrack = func(row, cols, diag1, diag2 int) {
		if row == n {
			board := make([]string, n)
			rowBuf := make([]byte, n)
			for r := 0; r < n; r++ {
				for j := range rowBuf {
					rowBuf[j] = '.'
				}
				rowBuf[queens[r]] = 'Q'
				board[r] = string(rowBuf)
			}
			out = append(out, board)
			return
		}
		// Go uses &^ for AND-NOT (no unary ~ operator).
		available := ((1 << n) - 1) &^ (cols | diag1 | diag2)
		for available != 0 {
			bit := available & -available
			// Trailing-zero count for the column index.
			col := 0
			for b := bit; b > 1; b >>= 1 {
				col++
			}
			queens[row] = col
			backtrack(row+1, cols|bit, (diag1|bit)<<1, (diag2|bit)>>1)
			available &= available - 1
		}
	}
	backtrack(0, 0, 0, 0)
	return out
}

func TotalNQueens(n int) int {
	count := 0
	var backtrack func(row, cols, diag1, diag2 int)
	backtrack = func(row, cols, diag1, diag2 int) {
		if row == n {
			count++
			return
		}
		available := ((1 << n) - 1) &^ (cols | diag1 | diag2)
		for available != 0 {
			bit := available & -available
			backtrack(row+1, cols|bit, (diag1|bit)<<1, (diag2|bit)>>1)
			available &= available - 1
		}
	}
	backtrack(0, 0, 0, 0)
	return count
}
