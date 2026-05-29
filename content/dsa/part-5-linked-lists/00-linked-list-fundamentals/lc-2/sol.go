// LC 2. Add Two Numbers
// Synchronized two-list walk with carry propagation. The dummy head
// lets every iteration append unconditionally; returning dummy.Next
// skips the sentinel.
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	carry := 0
	for l1 != nil || l2 != nil || carry != 0 {
		v1, v2 := 0, 0
		if l1 != nil {
			v1 = l1.Val
		}
		if l2 != nil {
			v2 = l2.Val
		}
		total := v1 + v2 + carry
		carry = total / 10
		tail.Next = &ListNode{Val: total % 10}
		tail = tail.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	return dummy.Next
}
