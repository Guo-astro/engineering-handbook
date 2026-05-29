// LC 695. Max Area of Island
package main

var dirs695 = [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func maxAreaOfIsland(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	rows, cols := len(grid), len(grid[0])
	best := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == 1 {
				area := bfsArea(grid, r, c, rows, cols)
				if area > best {
					best = area
				}
			}
		}
	}
	return best
}

func bfsArea(grid [][]int, sr, sc, rows, cols int) int {
	type cell struct{ r, c int }
	q := []cell{{sr, sc}}
	grid[sr][sc] = 0
	size := 0
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		size++
		for _, d := range dirs695 {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1 {
				grid[nr][nc] = 0
				q = append(q, cell{nr, nc})
			}
		}
	}
	return size
}
