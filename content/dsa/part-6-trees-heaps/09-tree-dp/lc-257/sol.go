// LC 257. Binary Tree Paths
package main

import "strconv"

// TreeNode is the canonical LeetCode binary-tree shape.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Shape 1 of tree DP: accumulator on the call stack. Go's immutable strings
// make backtracking implicit — each recursive call rebinds its own `path`
// local, so siblings naturally see a clean prefix.
func binaryTreePaths(root *TreeNode) []string {
	out := []string{}
	if root == nil {
		return out
	}
	var walk func(node *TreeNode, path string)
	walk = func(node *TreeNode, path string) {
		if path == "" {
			path = strconv.Itoa(node.Val)
		} else {
			path = path + "->" + strconv.Itoa(node.Val)
		}
		if node.Left == nil && node.Right == nil {
			out = append(out, path)
			return
		}
		if node.Left != nil {
			walk(node.Left, path)
		}
		if node.Right != nil {
			walk(node.Right, path)
		}
	}
	walk(root, "")
	return out
}
