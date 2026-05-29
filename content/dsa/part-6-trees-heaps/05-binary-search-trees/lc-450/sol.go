// LC 450. Delete Node in a BST
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minNode(n *TreeNode) *TreeNode {
	for n.Left != nil {
		n = n.Left
	}
	return n
}

func DeleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}
	if key < root.Val {
		root.Left = DeleteNode(root.Left, key)
	} else if key > root.Val {
		root.Right = DeleteNode(root.Right, key)
	} else {
		if root.Left == nil && root.Right == nil {
			return nil // case 1
		}
		if root.Left == nil {
			return root.Right // case 2a
		}
		if root.Right == nil {
			return root.Left // case 2b
		}
		succ := minNode(root.Right) // case 3
		root.Val = succ.Val
		root.Right = DeleteNode(root.Right, succ.Val)
	}
	return root
}
