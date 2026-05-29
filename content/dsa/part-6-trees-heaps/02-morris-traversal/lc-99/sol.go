// LC 99. Recover Binary Search Tree

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// RecoverTree fixes a BST in which exactly two nodes have been swapped,
// in O(1) auxiliary space.
//
// Reference: J. M. Morris, "Traversing binary trees simply and cheaply",
// Information Processing Letters 9(5):197-200, 1979.
//
// Layers the LC 99 "two witnesses" pattern on top of Morris inorder:
// track prev across the visit step; capture first on the first violation;
// keep updating second on every violation; swap at the end.
func RecoverTree(root *TreeNode) {
	var first, second, prev *TreeNode

	curr := root
	for curr != nil {
		if curr.Left == nil {
			if prev != nil && curr.Val < prev.Val {
				if first == nil {
					first = prev
				}
				second = curr
			}
			prev = curr
			curr = curr.Right
		} else {
			pred := curr.Left
			for pred.Right != nil && pred.Right != curr {
				pred = pred.Right
			}
			if pred.Right == nil {
				pred.Right = curr // install thread
				curr = curr.Left
			} else {
				pred.Right = nil // tear down before visit
				if prev != nil && curr.Val < prev.Val {
					if first == nil {
						first = prev
					}
					second = curr
				}
				prev = curr
				curr = curr.Right
			}
		}
	}

	if first != nil && second != nil {
		first.Val, second.Val = second.Val, first.Val
	}
}
