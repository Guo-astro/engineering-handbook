// LC 787. Cheapest Flights Within K Stops
package main

import "math"

func FindCheapestPrice(n int, flights [][]int, src, dst, k int) int {
    const INF = math.MaxInt32
    dist := make([]int, n)
    for i := range dist {
        dist[i] = INF
    }
    dist[src] = 0
    for i := 0; i <= k; i++ {
        // "previous-pass" view enforces the edge-count bound
        snapshot := make([]int, n)
        copy(snapshot, dist)
        for _, f := range flights {
            u, v, w := f[0], f[1], f[2]
            if snapshot[u] == INF {
                continue
            }
            if snapshot[u]+w < dist[v] {
                dist[v] = snapshot[u] + w
            }
        }
    }
    if dist[dst] == INF {
        return -1
    }
    return dist[dst]
}
