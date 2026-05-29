// LC 1368. Minimum Cost to Make at Least One Valid Path in a Grid
package main

import (
	"container/list"
	"math"
)

type cell struct{ r, c int }

func minCost(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	dr := [5]int{0, 0, 0, 1, -1}
	dc := [5]int{0, 1, -1, 0, 0}

	dist := make([][]int, rows)
	for i := range dist {
		dist[i] = make([]int, cols)
		for j := range dist[i] {
			dist[i][j] = math.MaxInt32
		}
	}
	dist[0][0] = 0

	dq := list.New()
	dq.PushFront(cell{0, 0})
	for dq.Len() > 0 {
		front := dq.Front()
		dq.Remove(front)
		cur := front.Value.(cell)
		r, c := cur.r, cur.c
		for d := 1; d <= 4; d++ {
			nr, nc := r+dr[d], c+dc[d]
			if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
				continue
			}
			cost := 1
			if grid[r][c] == d {
				cost = 0
			}
			nd := dist[r][c] + cost
			if nd < dist[nr][nc] {
				dist[nr][nc] = nd
				if cost == 0 {
					dq.PushFront(cell{nr, nc})
				} else {
					dq.PushBack(cell{nr, nc})
				}
			}
		}
	}
	return dist[rows-1][cols-1]
}
