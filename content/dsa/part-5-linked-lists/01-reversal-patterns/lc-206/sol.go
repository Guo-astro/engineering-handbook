// LC 206. Reverse Linked List
package main

// ListNode is a singly-linked list node (LC's canonical Go signature).
type ListNode struct {
	Val  int
	Next *ListNode
}

// reverseListIterative performs the prev/curr/next three-pointer reversal.
// Time O(n), space O(1).
func reverseListIterative(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}

// reverseListRecursive inverts the tail then rewires head.Next.Next = head.
// Time O(n), space O(n) on the call stack.
func reverseListRecursive(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	newHead := reverseListRecursive(head.Next)
	head.Next.Next = head
	head.Next = nil
	return newHead
}
