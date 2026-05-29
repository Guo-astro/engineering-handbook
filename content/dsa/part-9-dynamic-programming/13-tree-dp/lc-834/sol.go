// LC 834. Sum of Distances in Tree
// implements the re-rooting technique sketched in
//  (pattern extension).
package main

// sumOfDistancesInTree returns answer[i] = sum of distances from i to all
// other nodes. Two passes; O(n) total.
func sumOfDistancesInTree(n int, edges [][]int) []int {
	if n == 1 {
		return []int{0}
	}
	adj := make([][]int, n)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		adj[e[1]] = append(adj[e[1]], e[0])
	}
	count := make([]int, n)
	answer := make([]int, n)
	for i := range count {
		count[i] = 1
	}

	// Pass 1: post-order DFS — fill count[] and answer[0].
	var post func(u, parent int)
	post = func(u, parent int) {
		for _, v := range adj[u] {
			if v == parent {
				continue
			}
			post(v, u)
			count[u] += count[v]
			answer[u] += answer[v] + count[v]
		}
	}

	// Pass 2: pre-order DFS — re-root from u to each child v in O(1).
	var pre func(u, parent int)
	pre = func(u, parent int) {
		for _, v := range adj[u] {
			if v == parent {
				continue
			}
			// count[v] nodes get 1 closer; (n - count[v]) get 1 farther.
			answer[v] = answer[u] - count[v] + (n - count[v])
			pre(v, u)
		}
	}

	post(0, -1)
	pre(0, -1)
	return answer
}
