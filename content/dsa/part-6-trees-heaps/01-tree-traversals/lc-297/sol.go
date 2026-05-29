// LC 297. Serialize and Deserialize Binary Tree
// Codec: preorder DFS + "#" sentinel for null children; round-trip is a same-shaped
// preorder DFS reading from an iterator over the tokens.
package main

import (
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

const (
	nullTok = "#"
	sepTok  = ","
)

// Serialize — preorder DFS; emit value or null token for each slot.
func Serialize(root *TreeNode) string {
	parts := []string{}
	var dfs func(n *TreeNode)
	dfs = func(n *TreeNode) {
		if n == nil {
			parts = append(parts, nullTok)
			return
		}
		parts = append(parts, strconv.Itoa(n.Val)) // visit (preorder)
		dfs(n.Left)
		dfs(n.Right)
	}
	dfs(root)
	return strings.Join(parts, sepTok)
}

// Deserialize — same preorder shape; consume one token per slot.
func Deserialize(data string) *TreeNode {
	tokens := strings.Split(data, sepTok)
	idx := 0
	var build func() *TreeNode
	build = func() *TreeNode {
		if idx >= len(tokens) {
			return nil
		}
		tok := tokens[idx]
		idx++
		if tok == nullTok {
			return nil
		}
		v, _ := strconv.Atoi(tok)
		node := &TreeNode{Val: v}
		node.Left = build()
		node.Right = build()
		return node
	}
	return build()
}
