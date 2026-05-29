// LC 212. Word Search II
// Trie-accelerated DFS on the grid; missing
// trie child = instant backtrack. After finding a word, clear the
// stored word to suppress re-finding.
package main

type wsNode struct {
	children map[byte]*wsNode
	word     string
}

func findWords(board [][]byte, words []string) []string {
	root := &wsNode{children: map[byte]*wsNode{}}
	for _, w := range words {
		node := root
		for i := 0; i < len(w); i++ {
			ch := w[i]
			if node.children[ch] == nil {
				node.children[ch] = &wsNode{children: map[byte]*wsNode{}}
			}
			node = node.children[ch]
		}
		node.word = w
	}

	var found []string
	rows, cols := len(board), len(board[0])

	var dfs func(r, c int, parent *wsNode)
	dfs = func(r, c int, parent *wsNode) {
		ch := board[r][c]
		node := parent.children[ch]
		if node == nil {
			return
		}
		if node.word != "" {
			found = append(found, node.word)
			node.word = ""
		}
		board[r][c] = '#'
		dirs := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] != '#' {
				dfs(nr, nc, node)
			}
		}
		board[r][c] = ch
		if len(node.children) == 0 {
			delete(parent.children, ch)
		}
	}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			dfs(r, c, root)
		}
	}
	return found
}
