// LC 886. Possible Bipartition
// Build adjacency from 1-indexed dislikes, then run standard 2-coloring BFS.
package main

func possibleBipartition(n int, dislikes [][]int) bool {
    graph := make([][]int, n+1) // 1-indexed; slot 0 unused
    for _, d := range dislikes {
        graph[d[0]] = append(graph[d[0]], d[1])
        graph[d[1]] = append(graph[d[1]], d[0])
    }

    color := make([]int, n+1) // 0 = unvisited, 1 / -1 = two groups
    for start := 1; start <= n; start++ {
        if color[start] != 0 {
            continue
        }
        color[start] = 1
        q := []int{start}
        for len(q) > 0 {
            u := q[0]
            q = q[1:]
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
