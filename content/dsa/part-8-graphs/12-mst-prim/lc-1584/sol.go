// LC 1584. Min Cost to Connect All Points
package main

import "container/heap"

type pqItem struct{ w, v int }
type minHeap []pqItem

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].w < h[j].w }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(pqItem)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func minCostConnectPoints(points [][]int) int {
	n := len(points)
	if n <= 1 {
		return 0
	}
	inMST := make([]bool, n)
	pq := &minHeap{}
	heap.Init(pq)
	heap.Push(pq, pqItem{0, 0})       // (weight, vertex)
	total, edgesAdded := 0, 0
	for pq.Len() > 0 && edgesAdded < n {
		top := heap.Pop(pq).(pqItem)
		w, u := top.w, top.v
		if inMST[u] {
			continue                   // stale entry
		}
		inMST[u] = true
		total += w
		edgesAdded++
		for v := 0; v < n; v++ {
			if !inMST[v] {
				d := abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
				heap.Push(pq, pqItem{d, v})
			}
		}
	}
	return total
}
