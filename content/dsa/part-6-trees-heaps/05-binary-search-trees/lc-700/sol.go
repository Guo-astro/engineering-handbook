// LC 700. Search in a Binary Search Tree
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func SearchBST(root *TreeNode, target int) *TreeNode {
	cur := root
	for cur != nil {
		if target == cur.Val {
			return cur
		}
		if target < cur.Val {
			cur = cur.Left
		} else {
			cur = cur.Right
		}
	}
	return nil
}
