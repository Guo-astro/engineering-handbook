// LC 200. Number of Islands
package main

var dirs = [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func numIslands(grid [][]byte) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	rows, cols := len(grid), len(grid[0])
	count := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == '1' {
				count++
				bfs(grid, r, c, rows, cols)
			}
		}
	}
	return count
}

func bfs(grid [][]byte, sr, sc, rows, cols int) {
	type cell struct{ r, c int }
	// Slice-as-queue is idiomatic in Go; container/list is overkill here.
	q := []cell{{sr, sc}}
	grid[sr][sc] = '0'
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1' {
				grid[nr][nc] = '0'
				q = append(q, cell{nr, nc})
			}
		}
	}
}
