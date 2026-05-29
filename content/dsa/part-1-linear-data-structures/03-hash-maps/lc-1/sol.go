// LC 1. Two Sum
// One pass with a value -> first-seen-index map. Look up the complement
// BEFORE inserting; the lookup-then-insert order prevents matching an
// element against itself on inputs like [3, 3]. O(n) time, O(n) space.
package main

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
