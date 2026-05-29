// LC 124. Binary Tree Maximum Path Sum
package main

import "math"

// TreeNode is the standard LC binary-tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// maxPathSum returns the maximum sum of any non-empty path in the tree.
// A path may bend at one node; it cannot bend twice. The dual-quantity
// split is what enforces that constraint correctly.
func maxPathSum(root *TreeNode) int {
	best := math.MinInt32
	var gain func(node *TreeNode) int
	gain = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		leftGain := max(gain(node.Left), 0)
		rightGain := max(gain(node.Right), 0)
		// Bent path through node — compared to global, NOT returned.
		if v := node.Val + leftGain + rightGain; v > best {
			best = v
		}
		// Straight-down path returned to parent.
		return node.Val + max(leftGain, rightGain)
	}
	gain(root)
	return best
}
