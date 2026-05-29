// LC 25. Reverse Nodes in k-Group
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{Next: head}
	groupPrev := dummy

	for {
		kth := kthAfter(groupPrev, k)
		if kth == nil {
			break
		}
		groupNext := kth.Next

		var prev *ListNode = groupNext
		curr := groupPrev.Next
		for curr != groupNext {
			nxt := curr.Next
			curr.Next = prev
			prev = curr
			curr = nxt
		}

		newGroupTail := groupPrev.Next
		groupPrev.Next = kth
		groupPrev = newGroupTail
	}

	return dummy.Next
}

func kthAfter(node *ListNode, k int) *ListNode {
	curr := node
	for curr != nil && k > 0 {
		curr = curr.Next
		k--
	}
	return curr
}
