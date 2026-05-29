// LC 39. Combination Sum
// mechanism (recurse with i, not i+1, to allow reuse).
package main

import "sort"

func CombinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates) // sort enables the early break below
	result := [][]int{}
	path := []int{}
	var dfs func(start, remaining int)
	dfs = func(start, remaining int) {
		if remaining == 0 {
			// snapshot when target hit exactly; clone because slices alias backing array
			snap := make([]int, len(path))
			copy(snap, path)
			result = append(result, snap)
			return
		}
		for i := start; i < len(candidates); i++ {
			if candidates[i] > remaining {
				break // sorted: no later candidate fits either
			}
			path = append(path, candidates[i])
			dfs(i, remaining-candidates[i]) // i, not i+1 — reuse same element
			path = path[:len(path)-1]       // undo for backtrack
		}
	}
	dfs(0, target)
	return result
}
