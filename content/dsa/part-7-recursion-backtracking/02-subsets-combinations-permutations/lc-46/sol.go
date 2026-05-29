// LC 46. Permutations
// mechanism pseudocode and §5.3.
package main

func Permute(nums []int) [][]int {
	result := [][]int{}
	path := []int{}
	used := make([]bool, len(nums))
	var dfs func()
	dfs = func() {
		if len(path) == len(nums) {
			// snapshot only at full-length leaves; clone because slices alias backing array
			snap := make([]int, len(path))
			copy(snap, path)
			result = append(result, snap)
			return
		}
		for i := 0; i < len(nums); i++ {
			if used[i] {
				continue // element already in path; skip
			}
			used[i] = true
			path = append(path, nums[i])
			dfs()
			path = path[:len(path)-1] // undo for backtrack
			used[i] = false
		}
	}
	dfs()
	return result
}
