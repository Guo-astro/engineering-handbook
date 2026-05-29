// LC 295. Find Median from Data Stream
// Two-heap technique with explicit MaxHeapInt and MinHeapInt over container/heap.
package main

import "container/heap"

type MinHeapInt []int

func (h MinHeapInt) Len() int           { return len(h) }
func (h MinHeapInt) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeapInt) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeapInt) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinHeapInt) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

type MaxHeapInt []int

func (h MaxHeapInt) Len() int           { return len(h) }
func (h MaxHeapInt) Less(i, j int) bool { return h[i] > h[j] }     // flip
func (h MaxHeapInt) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeapInt) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MaxHeapInt) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

type MedianFinder struct {
	lower MaxHeapInt
	upper MinHeapInt
}

func NewMedianFinder() *MedianFinder { return &MedianFinder{} }

func (m *MedianFinder) AddNum(num int) {
	heap.Push(&m.lower, num)
	heap.Push(&m.upper, heap.Pop(&m.lower).(int))
	if m.upper.Len() > m.lower.Len() {
		heap.Push(&m.lower, heap.Pop(&m.upper).(int))
	}
}

func (m *MedianFinder) FindMedian() float64 {
	if m.lower.Len() > m.upper.Len() {
		return float64(m.lower[0])
	}
	return (float64(m.lower[0]) + float64(m.upper[0])) / 2.0
}
