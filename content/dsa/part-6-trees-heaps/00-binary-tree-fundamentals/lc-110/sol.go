// LC 110. Balanced Binary Tree
//.
// LC 110 Balanced Binary Tree, height-or-sentinel post-order recursion.
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	return height(root) != -1
}

func height(node *TreeNode) int {
	if node == nil {
		return 0
	}
	lh := height(node.Left)
	if lh == -1 {
		return -1
	}
	rh := height(node.Right)
	if rh == -1 {
		return -1
	}
	diff := lh - rh
	if diff < 0 {
		diff = -diff
	}
	if diff > 1 {
		return -1
	}
	if lh > rh {
		return 1 + lh
	}
	return 1 + rh
}
