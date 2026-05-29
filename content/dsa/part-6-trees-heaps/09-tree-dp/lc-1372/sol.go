// LC 1372. Longest ZigZag Path in a Binary Tree
package main

// Shape 3 of tree DP (diameter trick) + shape 4 (tuple return).
// Go closure over `best` is the natural idiom; a 2-int slice carries the
// (leftExtending, rightExtending) tuple back up the recursion.
func longestZigZag(root *TreeNode) int {
	if root == nil {
		return 0
	}
	best := 0
	var helper func(node *TreeNode) (int, int)
	helper = func(node *TreeNode) (int, int) {
		if node == nil {
			return -1, -1 // sentinel: no chain to extend
		}
		_, leftRight := helper(node.Left)
		rightLeft, _ := helper(node.Right)
		// Each child contributes the chain ending in the OTHER direction.
		leftLen := leftRight + 1
		rightLen := rightLeft + 1
		localBest := leftLen
		if rightLen > localBest {
			localBest = rightLen
		}
		if localBest > best {
			best = localBest
		}
		return leftLen, rightLen
	}
	helper(root)
	return best
}
