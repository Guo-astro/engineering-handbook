// LC 847. Shortest Path Visiting All Nodes
// Bitmask BFS over (node, mask) states. n <= 12; state space n * 2^n.
// O(n^2 * 2^n) time, O(n * 2^n) space.
package main

func shortestPathLength(graph [][]int) int {
	n := len(graph)
	if n == 1 {
		return 0
	}
	fullMask := (1 << n) - 1

	visited := make([][]bool, n)
	for i := range visited {
		visited[i] = make([]bool, 1<<n)
	}

	type state struct {
		node, mask, dist int
	}
	queue := make([]state, 0, n*(1<<n))
	for i := 0; i < n; i++ {
		startMask := 1 << i
		visited[i][startMask] = true
		queue = append(queue, state{i, startMask, 0})
	}

	for len(queue) > 0 {
		s := queue[0]
		queue = queue[1:]
		if s.mask == fullMask {
			return s.dist
		}
		for _, nb := range graph[s.node] {
			newMask := s.mask | (1 << nb)
			if !visited[nb][newMask] {
				visited[nb][newMask] = true
				queue = append(queue, state{nb, newMask, s.dist + 1})
			}
		}
	}

	return -1 // LC constraints guarantee connectivity; defensive.
}
