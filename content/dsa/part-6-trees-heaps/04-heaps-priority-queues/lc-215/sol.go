// LC 215. Kth Largest Element in an Array
// heap solution mirrors.
// container/heap requires Len/Less/Swap/Push/Pop; min-heap via Less = a < b.
package main

import "container/heap"

type MinHeapInt []int

func (h MinHeapInt) Len() int           { return len(h) }
func (h MinHeapInt) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeapInt) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeapInt) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinHeapInt) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

func findKthLargest(nums []int, k int) int {
	h := &MinHeapInt{}
	heap.Init(h)
	for _, x := range nums {
		if h.Len() < k {
			heap.Push(h, x)
		} else if x > (*h)[0] {
			(*h)[0] = x
			heap.Fix(h, 0)
		}
	}
	return (*h)[0]
}
