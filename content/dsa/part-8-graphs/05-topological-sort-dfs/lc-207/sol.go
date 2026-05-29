// LC 207. Course Schedule
package main

const (
	white = 0
	gray  = 1
	black = 2
)

func canFinish(numCourses int, prerequisites [][]int) bool {
	adj := make([][]int, numCourses)
	for _, e := range prerequisites {
		a, b := e[0], e[1] // b -> a
		adj[b] = append(adj[b], a)
	}
	color := make([]int, numCourses)
	var dfs func(u int) bool
	dfs = func(u int) bool {
		color[u] = gray
		for _, v := range adj[u] {
			if color[v] == gray {
				return false
			}
			if color[v] == white && !dfs(v) {
				return false
			}
		}
		color[u] = black
		return true
	}
	for u := 0; u < numCourses; u++ {
		if color[u] == white && !dfs(u) {
			return false
		}
	}
	return true
}
