// LC 1042. Flower Planting With No Adjacent
// NOT a 2-coloring: 4 flower types over a max-degree-3 graph (greedy works).
package main

func gardenNoAdj(n int, paths [][]int) []int {
    graph := make([][]int, n+1) // 1-indexed
    for _, p := range paths {
        graph[p[0]] = append(graph[p[0]], p[1])
        graph[p[1]] = append(graph[p[1]], p[0])
    }

    answer := make([]int, n+1) // 0 = unassigned; flowers 1..4
    for u := 1; u <= n; u++ {
        var used [5]bool
        for _, v := range graph[u] {
            if answer[v] != 0 {
                used[answer[v]] = true
            }
        }
        for flower := 1; flower <= 4; flower++ {
            if !used[flower] {
                answer[u] = flower
                break
            }
        }
    }
    return answer[1:]
}
