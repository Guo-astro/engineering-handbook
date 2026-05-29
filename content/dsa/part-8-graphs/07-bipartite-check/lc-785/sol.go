// LC 785. Is Graph Bipartite?
package main

func isBipartite(graph [][]int) bool {
    n := len(graph)
    color := make([]int, n) // 0 = unvisited, 1 / -1 = two classes
    for start := 0; start < n; start++ {
        if color[start] != 0 {
            continue
        }
        color[start] = 1
        q := []int{start} // small slice queue; OK at LC 785 cap n <= 100
        for len(q) > 0 {
            u := q[0]
            q = q[1:] // O(1) amortized via underlying-array offset
            for _, v := range graph[u] {
                if color[v] == 0 {
                    color[v] = -color[u]
                    q = append(q, v)
                } else if color[v] == color[u] {
                    return false
                }
            }
        }
    }
    return true
}
