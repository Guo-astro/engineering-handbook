// LC 94. Binary Tree Inorder Traversal
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// InorderTraversal — recursive, the canonical LC 94 entry point.
func InorderTraversal(root *TreeNode) []int {
	out := []int{}
	var dfs func(*TreeNode)
	dfs = func(n *TreeNode) {
		if n == nil {
			return
		}
		dfs(n.Left)
		out = append(out, n.Val) // visit
		dfs(n.Right)
	}
	dfs(root)
	return out
}

// InorderIterative — push left chain, pop, pivot right.
func InorderIterative(root *TreeNode) []int {
	out := []int{}
	stack := []*TreeNode{}
	cur := root
	for cur != nil || len(stack) > 0 {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		out = append(out, cur.Val)
		cur = cur.Right // pivot to right subtree
	}
	return out
}

// PreorderIterative — push right BEFORE left so left pops next.
func PreorderIterative(root *TreeNode) []int {
	out := []int{}
	if root == nil {
		return out
	}
	stack := []*TreeNode{root}
	for len(stack) > 0 {
		n := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		out = append(out, n.Val)
		if n.Right != nil {
			stack = append(stack, n.Right)
		}
		if n.Left != nil {
			stack = append(stack, n.Left)
		}
	}
	return out
}

// PostorderIterative — two-stack / reverse trick.
func PostorderIterative(root *TreeNode) []int {
	out := []int{}
	if root == nil {
		return out
	}
	stack := []*TreeNode{root}
	for len(stack) > 0 {
		n := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		out = append(out, n.Val)
		if n.Left != nil {
			stack = append(stack, n.Left)
		}
		if n.Right != nil {
			stack = append(stack, n.Right)
		}
	}
	for i, j := 0, len(out)-1; i < j; i, j = i+1, j-1 {
		out[i], out[j] = out[j], out[i]
	}
	return out
}
