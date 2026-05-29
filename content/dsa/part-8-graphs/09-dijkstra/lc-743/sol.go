// LC 743. Network Delay Time
package main

import (
	"container/heap"
	"math"
)

type pqItem struct{ dist, node int }
type minHeap []pqItem

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(pqItem)) }
func (h *minHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[: n-1]
	return x
}

func networkDelayTime(times [][]int, n, k int) int {
	adj := make([][][2]int, n+1)
	for _, e := range times {
		adj[e[0]] = append(adj[e[0]], [2]int{e[1], e[2]})
	}
	const INF = math.MaxInt32
	dist := make([]int, n+1)
	for i := range dist {
		dist[i] = INF
	}
	dist[k] = 0

	pq := &minHeap{{0, k}}
	heap.Init(pq)
	for pq.Len() > 0 {
		cur := heap.Pop(pq).(pqItem)
		d, u := cur.dist, cur.node
		if d > dist[u] {
			continue // lazy-deletion
		}
		for _, vw := range adj[u] {
			v, w := vw[0], vw[1]
			nd := d + w
			if nd < dist[v] {
				dist[v] = nd
				heap.Push(pq, pqItem{nd, v})
			}
		}
	}

	longest := 0
	for i := 1; i <= n; i++ {
		if dist[i] == INF {
			return -1
		}
		if dist[i] > longest {
			longest = dist[i]
		}
	}
	return longest
}
