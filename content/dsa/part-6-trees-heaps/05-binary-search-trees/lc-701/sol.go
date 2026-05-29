// LC 701. Insert into a Binary Search Tree
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func InsertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{Val: val}
	}
	if val < root.Val {
		root.Left = InsertIntoBST(root.Left, val)
	} else if val > root.Val {
		root.Right = InsertIntoBST(root.Right, val)
	}
	// Duplicate: no-op.
	return root
}
