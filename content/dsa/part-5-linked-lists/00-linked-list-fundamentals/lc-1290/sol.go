// LC 1290. Convert Binary Number in a Linked List to Integer
// Single-pass walk with a running accumulator. Each node holds 0 or 1;
// shift the result left and OR in the current bit.
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	result := 0
	curr := head
	for curr != nil {
		result = (result << 1) | curr.Val
		curr = curr.Next
	}
	return result
}
