// LC 79. Word Search
package main

func exist(board [][]byte, word string) bool {
	if len(board) == 0 || len(board[0]) == 0 || len(word) == 0 {
		return false
	}
	rows, cols := len(board), len(board[0])
	var dfs func(r, c, k int) bool
	dfs = func(r, c, k int) bool {
		if k == len(word) {
			return true
		}
		if r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[k] {
			return false
		}
		saved := board[r][c]
		board[r][c] = '#' // sentinel never matches a real word char
		found := dfs(r+1, c, k+1) || dfs(r-1, c, k+1) ||
			dfs(r, c+1, k+1) || dfs(r, c-1, k+1)
		board[r][c] = saved // restore on backtrack
		return found
	}
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if board[r][c] == word[0] && dfs(r, c, 0) {
				return true
			}
		}
	}
	return false
}
