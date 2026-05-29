// LC 78. Subsets
package main

func Subsets(nums []int) [][]int {
	result := [][]int{}
	path := []int{}
	var dfs func(start int)
	dfs = func(start int) {
		// snapshot at every node; clone because slices alias backing array
		snap := make([]int, len(path))
		copy(snap, path)
		result = append(result, snap)
		for i := start; i < len(nums); i++ {
			path = append(path, nums[i])
			dfs(i + 1) // i+1 prevents reuse and reordering
			path = path[:len(path)-1]
		}
	}
	dfs(0)
	return result
}
