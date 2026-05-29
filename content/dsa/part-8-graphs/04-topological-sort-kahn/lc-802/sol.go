// LC 802. Find Eventual Safe States
package main

func eventualSafeNodes(graph [][]int) []int {
	n := len(graph)
	revIndeg := make([]int, n) // = original out-degree
	revAdj := make([][]int, n)
	for u, succs := range graph {
		for _, v := range succs {
			revAdj[v] = append(revAdj[v], u) // reverse edge v -> u
			revIndeg[u]++
		}
	}
	q := make([]int, 0, n)
	for v := 0; v < n; v++ {
		if revIndeg[v] == 0 {
			q = append(q, v)
		}
	}
	safe := make([]bool, n)
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		safe[u] = true
		for _, v := range revAdj[u] {
			revIndeg[v]--
			if revIndeg[v] == 0 {
				q = append(q, v)
			}
		}
	}
	ans := make([]int, 0)
	for v := 0; v < n; v++ {
		if safe[v] {
			ans = append(ans, v)
		}
	}
	return ans
}
