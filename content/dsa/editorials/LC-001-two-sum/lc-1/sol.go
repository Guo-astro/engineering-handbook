// LC 1. Two Sum
package main

// twoSum implements LC 1 in O(n) using a hash map of value -> index.
func twoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))
	for i, x := range nums {
		complement := target - x
		if j, ok := seen[complement]; ok {
			return []int{j, i}
		}
		seen[x] = i
	}
	return nil
}
