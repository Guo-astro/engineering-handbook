// LC 23. Merge k Sorted Lists
package main

import "container/heap"

// ListNode is the canonical LC singly-linked list node in Go.
type ListNode struct {
	Val  int
	Next *ListNode
}

// cursorEntry: (Val, ListIndex, Node). ListIndex is the tiebreak key.
type cursorEntry struct {
	val  int
	idx  int
	node *ListNode
}

type cursorHeap []cursorEntry

func (h cursorHeap) Len() int { return len(h) }
func (h cursorHeap) Less(i, j int) bool {
	if h[i].val != h[j].val {
		return h[i].val < h[j].val
	}
	return h[i].idx < h[j].idx
}
func (h cursorHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *cursorHeap) Push(x any)   { *h = append(*h, x.(cursorEntry)) }
func (h *cursorHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// MergeKListsHeap merges k sorted lists via a min-heap of cursors.
// Each of the N total nodes is pushed and popped at most once; each
// heap op is O(log k). O(N log k) time, O(k) auxiliary.
func MergeKListsHeap(lists []*ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	h := &cursorHeap{}
	heap.Init(h)
	for i, head := range lists {
		if head != nil {
			heap.Push(h, cursorEntry{val: head.Val, idx: i, node: head})
		}
	}
	for h.Len() > 0 {
		top := heap.Pop(h).(cursorEntry)
		tail.Next = top.node
		tail = tail.Next
		if top.node.Next != nil {
			heap.Push(h, cursorEntry{val: top.node.Next.Val, idx: top.idx, node: top.node.Next})
		}
	}
	tail.Next = nil
	return dummy.Next
}

// MergeKListsDivideConquer pairs lists up and merges in a balanced
// binary tree. log k merge levels, O(N) work per level. O(N log k)
// time, O(log k) recursion stack.
func MergeKListsDivideConquer(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}
	current := lists
	for len(current) > 1 {
		merged := make([]*ListNode, 0, (len(current)+1)/2)
		for i := 0; i < len(current); i += 2 {
			var b *ListNode
			if i+1 < len(current) {
				b = current[i+1]
			}
			merged = append(merged, mergeTwo(current[i], b))
		}
		current = merged
	}
	return current[0]
}

// mergeTwo is LC 21's iterative merge, used as the leaf of d-and-c.
func mergeTwo(a, b *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for a != nil && b != nil {
		if a.Val <= b.Val {
			tail.Next = a
			a = a.Next
		} else {
			tail.Next = b
			b = b.Next
		}
		tail = tail.Next
	}
	if a != nil {
		tail.Next = a
	} else {
		tail.Next = b
	}
	return dummy.Next
}
