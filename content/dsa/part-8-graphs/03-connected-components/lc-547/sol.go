// LC 547. Number of Provinces
package main

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	visited := make([]bool, n)
	count := 0
	for i := 0; i < n; i++ {
		if !visited[i] {
			count++
			bfs(isConnected, visited, i, n)
		}
	}
	return count
}

func bfs(isConnected [][]int, visited []bool, start, n int) {
	q := []int{start}
	visited[start] = true
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for v := 0; v < n; v++ {
			if isConnected[u][v] == 1 && !visited[v] {
				visited[v] = true
				q = append(q, v)
			}
		}
	}
}
