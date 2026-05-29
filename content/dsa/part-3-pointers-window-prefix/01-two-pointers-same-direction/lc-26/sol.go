// LC 26. Remove Duplicates from Sorted Array
package main

// removeDuplicates implements LC 26: in-place dedup of a sorted slice.
// Invariant: nums[0..write) is a sorted prefix of distinct elements.
func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	write := 1
	for read := 1; read < len(nums); read++ {
		if nums[read] != nums[write-1] {
			nums[write] = nums[read]
			write++
		}
	}
	return write
}
