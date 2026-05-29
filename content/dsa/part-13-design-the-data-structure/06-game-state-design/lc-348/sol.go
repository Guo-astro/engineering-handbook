// LC 348. Design Tic-Tac-Toe

package main

type TicTacToe struct {
	n        int
	rows     []int
	cols     []int
	diag     int
	antiDiag int
}

func NewTicTacToe(n int) *TicTacToe {
	return &TicTacToe{
		n:    n,
		rows: make([]int, n),
		cols: make([]int, n),
	}
}

func (t *TicTacToe) Move(row, col, player int) int {
	delta := 1
	if player == 2 {
		delta = -1
	}
	t.rows[row] += delta
	t.cols[col] += delta
	if row == col {
		t.diag += delta
	}
	if row+col == t.n-1 {
		t.antiDiag += delta
	}

	target := t.n
	if player == 2 {
		target = -t.n
	}
	if t.rows[row] == target || t.cols[col] == target ||
		t.diag == target || t.antiDiag == target {
		return player
	}
	return 0
}
