// LC 136. Single Number

package main

// singleNumber returns the lone element when every other appears twice.
// O(n) time, O(1) space.
func singleNumber(nums []int) int {
	result := 0
	for _, x := range nums {
		result ^= x
	}
	return result
}
