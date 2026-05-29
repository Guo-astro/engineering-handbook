// LC 210. Course Schedule II
package main

func findOrder(numCourses int, prerequisites [][]int) []int {
	indeg := make([]int, numCourses)
	adj := make([][]int, numCourses)
	for _, e := range prerequisites {
		a, b := e[0], e[1] // b -> a
		adj[b] = append(adj[b], a)
		indeg[a]++
	}
	q := make([]int, 0, numCourses)
	for v := 0; v < numCourses; v++ {
		if indeg[v] == 0 {
			q = append(q, v)
		}
	}
	order := make([]int, 0, numCourses)
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		order = append(order, u)
		for _, v := range adj[u] {
			indeg[v]--
			if indeg[v] == 0 {
				q = append(q, v)
			}
		}
	}
	if len(order) != numCourses {
		return []int{}
	}
	return order
}
