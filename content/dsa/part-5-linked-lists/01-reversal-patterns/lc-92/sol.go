// LC 92. Reverse Linked List II
// One-pass head-insertion variant: walk a sentinel (left-1) steps to
// land just before the segment, then for (right-left) iterations splice
// each newly-encountered node to the front of the reversed prefix.
package main

// ListNode is a singly-linked list node (LC's canonical Go signature).
type ListNode struct {
	Val  int
	Next *ListNode
}

// reverseBetween performs a one-pass range reversal via head-insertion.
// Time O(n), space O(1).
func reverseBetween(head *ListNode, left, right int) *ListNode {
	if head == nil || left == right {
		return head
	}

	dummy := &ListNode{Next: head}
	pre := dummy
	for i := 0; i < left-1; i++ {
		pre = pre.Next
	}

	// `curr` is the first node of the segment to reverse; it stays put and
	// becomes the segment's tail. Each iteration lifts curr.Next out and
	// splices it to the front of the reversed prefix.
	curr := pre.Next
	for i := 0; i < right-left; i++ {
		moved := curr.Next
		curr.Next = moved.Next
		moved.Next = pre.Next
		pre.Next = moved
	}

	return dummy.Next
}
