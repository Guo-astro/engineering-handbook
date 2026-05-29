// LC 37. Sudoku Solver
package main

import "math/bits"

const allDigits = 0x1FF

type sudokuSolver struct {
	board [][]byte
	rows  [9]int
	cols  [9]int
	boxes [9]int
}

func boxIndex(r, c int) int { return (r/3)*3 + (c / 3) }

func solveSudoku(board [][]byte) {
	s := &sudokuSolver{board: board}
	for i := 0; i < 9; i++ {
		s.rows[i] = allDigits
		s.cols[i] = allDigits
		s.boxes[i] = allDigits
	}
	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			if board[r][c] != '.' {
				bit := 1 << (board[r][c] - '1')
				s.rows[r] ^= bit
				s.cols[c] ^= bit
				s.boxes[boxIndex(r, c)] ^= bit
			}
		}
	}
	s.backtrack()
}

func (s *sudokuSolver) backtrack() bool {
	bestR, bestC, bestCount, bestMask := -1, -1, 10, 0
	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			if s.board[r][c] != '.' {
				continue
			}
			cand := s.rows[r] & s.cols[c] & s.boxes[boxIndex(r, c)]
			cnt := bits.OnesCount(uint(cand))
			if cnt < bestCount {
				bestCount = cnt
				bestR, bestC, bestMask = r, c, cand
				if cnt <= 1 {
					break
				}
			}
		}
		if bestCount <= 1 {
			break
		}
	}
	if bestR == -1 {
		return true
	}
	if bestCount == 0 {
		return false
	}

	r, c, bx := bestR, bestC, boxIndex(bestR, bestC)
	cand := bestMask
	for cand != 0 {
		bit := cand & -cand
		cand ^= bit
		d := bits.TrailingZeros(uint(bit)) + 1
		s.board[r][c] = byte('0' + d)
		s.rows[r] ^= bit
		s.cols[c] ^= bit
		s.boxes[bx] ^= bit
		if s.backtrack() {
			return true
		}
		s.rows[r] ^= bit
		s.cols[c] ^= bit
		s.boxes[bx] ^= bit
		s.board[r][c] = '.'
	}
	return false
}
