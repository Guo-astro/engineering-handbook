// LC 508. Most Frequent Subtree Sum
package main

// Shape 2 of tree DP: post-order returns subtree sum; counts map captures
// every sum the recursion produces. Go's closure over `counts` and `best`
// is the natural idiom — no array wrapper, no class field.
func findFrequentTreeSum(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	counts := map[int]int{}
	best := 0
	var subtreeSum func(node *TreeNode) int
	subtreeSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		s := node.Val + subtreeSum(node.Left) + subtreeSum(node.Right)
		counts[s]++
		if counts[s] > best {
			best = counts[s]
		}
		return s
	}
	subtreeSum(root)
	res := []int{}
	for s, c := range counts {
		if c == best {
			res = append(res, s)
		}
	}
	return res
}
