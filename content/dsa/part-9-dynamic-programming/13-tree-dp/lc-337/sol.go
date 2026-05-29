// LC 337. House Robber III
// mirrors the two-state tuple-return pattern from
//  (pair-return state machine on tree).
package main

// TreeNode is the standard LC binary-tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// rob returns the maximum money the robber can take without alerting the
// police. The helper returns (robThis, skipThis) for each subtree; the
// wrapper takes the better of the two at the root.
func rob(root *TreeNode) int {
	var helper func(node *TreeNode) (int, int)
	helper = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}
		robL, skipL := helper(node.Left)
		robR, skipR := helper(node.Right)
		// robThis: take this node; both children MUST be skipped.
		robThis := node.Val + skipL + skipR
		// skipThis: take the better state at each child independently.
		skipThis := max(robL, skipL) + max(robR, skipR)
		return robThis, skipThis
	}
	robRoot, skipRoot := helper(root)
	return max(robRoot, skipRoot)
}
