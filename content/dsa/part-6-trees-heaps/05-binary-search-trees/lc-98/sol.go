// LC 98. Validate Binary Search Tree
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func IsValidBST(root *TreeNode) bool {
	// Nullable *int sentinels: nil means "no bound on this side".
	var check func(n *TreeNode, lo, hi *int) bool
	check = func(n *TreeNode, lo, hi *int) bool {
		if n == nil {
			return true
		}
		if lo != nil && n.Val <= *lo {
			return false
		}
		if hi != nil && n.Val >= *hi {
			return false
		}
		return check(n.Left, lo, &n.Val) && check(n.Right, &n.Val, hi)
	}
	return check(root, nil, nil)
}
