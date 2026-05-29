// LC 1361. Validate Binary Tree Nodes
package main

func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
	inDegree := make([]int, n)
	for _, c := range leftChild {
		if c != -1 {
			inDegree[c]++
		}
	}
	for _, c := range rightChild {
		if c != -1 {
			inDegree[c]++
		}
	}

	root := -1
	for i := 0; i < n; i++ {
		if inDegree[i] == 0 {
			if root != -1 {
				return false
			}
			root = i
		} else if inDegree[i] > 1 {
			return false
		}
	}
	if root == -1 {
		return false
	}

	seen := make([]bool, n)
	seen[root] = true
	visitedCount := 1
	queue := []int{root}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for _, v := range []int{leftChild[u], rightChild[u]} {
			if v == -1 {
				continue
			}
			if seen[v] {
				return false // cycle witness
			}
			seen[v] = true
			visitedCount++
			queue = append(queue, v)
		}
	}
	return visitedCount == n
}
