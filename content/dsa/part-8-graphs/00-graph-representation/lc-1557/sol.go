// LC 1557. Minimum Number of Vertices to Reach All Nodes
// In a DAG, a vertex is unreachable from any other vertex iff its in-degree
// is zero. The answer is the set of in-degree-zero vertices. No adjacency
// list is needed; a []int of size n is sufficient. O(V + E) time, O(V) space.
package main

func findSmallestSetOfVertices(n int, edges [][]int) []int {
	inDegree := make([]int, n)
	for _, e := range edges {
		inDegree[e[1]]++ // only the destination matters
	}
	out := make([]int, 0)
	for u := 0; u < n; u++ {
		if inDegree[u] == 0 {
			out = append(out, u)
		}
	}
	return out
}
