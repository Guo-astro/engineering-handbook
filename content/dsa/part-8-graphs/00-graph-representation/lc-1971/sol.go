// LC 1971. Find if Path Exists in Graph
// reachability cases match.
// Build an adjacency list from the edges, then BFS from source. Build and
// BFS are each O(V + E). Slice-of-slices is the idiomatic Go shape for
// dense integer vertex IDs; no map lookups in the hot loop.
package main

func validPath(n int, edges [][]int, source int, destination int) bool {
	if source == destination {
		return true
	}
	adj := make([][]int, n)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		adj[e[1]] = append(adj[e[1]], e[0]) // undirected: push both halves
	}
	visited := make([]bool, n)
	visited[source] = true
	q := []int{source}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range adj[u] {
			if v == destination {
				return true
			}
			if !visited[v] {
				visited[v] = true
				q = append(q, v)
			}
		}
	}
	return false
}
