// LC 23. Merge k Sorted Lists
// container/heap with a *ListNode-typed min-heap; Less compares h[i].Val.
package main

import "container/heap"

type ListNode struct {
	Val  int
	Next *ListNode
}

type MinHeapNode []*ListNode

func (h MinHeapNode) Len() int           { return len(h) }
func (h MinHeapNode) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h MinHeapNode) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeapNode) Push(x any)        { *h = append(*h, x.(*ListNode)) }
func (h *MinHeapNode) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

func mergeKLists(lists []*ListNode) *ListNode {
	h := &MinHeapNode{}
	heap.Init(h)
	for _, n := range lists {
		if n != nil {
			heap.Push(h, n)
		}
	}
	dummy := &ListNode{}
	tail := dummy
	for h.Len() > 0 {
		node := heap.Pop(h).(*ListNode)
		tail.Next = node
		tail = node
		if node.Next != nil {
			heap.Push(h, node.Next)
		}
	}
	tail.Next = nil
	return dummy.Next
}
