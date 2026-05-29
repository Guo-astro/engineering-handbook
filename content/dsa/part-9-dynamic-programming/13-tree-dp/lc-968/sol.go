// LC 968. Binary Tree Cameras
// mirrors the three-state DP pattern from research
// §5.6 (state-machine reduction on tree).
package main

// TreeNode is the standard LC binary-tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// State codes returned by dfs:
//
//	0 = NEEDS_COVER, 1 = HAS_CAMERA, 2 = COVERED
const (
	needsCover = 0
	hasCamera  = 1
	covered    = 2
)

func minCameraCover(root *TreeNode) int {
	cameras := 0
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return covered
		}
		l := dfs(node.Left)
		r := dfs(node.Right)
		// Any child unmonitored — place a camera here.
		if l == needsCover || r == needsCover {
			cameras++
			return hasCamera
		}
		// Any child holds a camera — this node is covered by it.
		if l == hasCamera || r == hasCamera {
			return covered
		}
		// Both children covered, none has a camera — this node needs cover.
		return needsCover
	}
	if dfs(root) == needsCover {
		cameras++
	}
	return cameras
}
