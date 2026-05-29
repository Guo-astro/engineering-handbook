// LC 994. Rotting Oranges
package main

func orangesRotting(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	rows, cols := len(grid), len(grid[0])
	type cell struct{ r, c, t int }
	queue := make([]cell, 0, rows*cols)
	fresh := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == 2 {
				queue = append(queue, cell{r, c, 0})
			} else if grid[r][c] == 1 {
				fresh++
			}
		}
	}
	if fresh == 0 {
		return 0
	}
	minutes := 0
	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		minutes = cur.t
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1 {
				grid[nr][nc] = 2
				fresh--
				queue = append(queue, cell{nr, nc, cur.t + 1})
			}
		}
	}
	if fresh == 0 {
		return minutes
	}
	return -1
}
