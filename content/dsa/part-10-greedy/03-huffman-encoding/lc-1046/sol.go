// LC 1046. Last Stone Weight
package main

import "container/heap"

// maxHeap of ints: Less is > so the largest sits at the root.
type maxHeap []int

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)         { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func lastStoneWeight(stones []int) int {
	h := &maxHeap{}
	for _, s := range stones {
		*h = append(*h, s)
	}
	heap.Init(h)
	for h.Len() > 1 {
		y := heap.Pop(h).(int) // heaviest
		x := heap.Pop(h).(int) // second heaviest
		if y != x {
			heap.Push(h, y-x)
		}
	}
	if h.Len() == 0 {
		return 0
	}
	return (*h)[0]
}
