// LC 21. Merge Two Sorted Lists
package main

// ListNode is the canonical LC singly-linked list node in Go.
type ListNode struct {
	Val  int
	Next *ListNode
}

// MergeTwoListsIterative splices the two sorted lists into one sorted
// list using the dummy + tail-pointer pattern. Stable: l1 wins on tie
// (`<=` not `<`). O(n + m) time, O(1) auxiliary.
func MergeTwoListsIterative(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{} // sentinel; never returned.
	tail := dummy
	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val { // `<=` keeps stability.
			tail.Next = l1
			l1 = l1.Next
		} else {
			tail.Next = l2
			l2 = l2.Next
		}
		tail = tail.Next
	}
	if l1 != nil {
		tail.Next = l1
	} else {
		tail.Next = l2
	}
	return dummy.Next
}

// MergeTwoListsRecursive is the textbook recursive form. O(n + m)
// call-stack space; prefer the iterative form for interview code.
func MergeTwoListsRecursive(l1, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	if l1.Val <= l2.Val {
		l1.Next = MergeTwoListsRecursive(l1.Next, l2)
		return l1
	}
	l2.Next = MergeTwoListsRecursive(l1, l2.Next)
	return l2
}
