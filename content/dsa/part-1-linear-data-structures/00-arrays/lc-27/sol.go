// LC 27. Remove Element
// Two-pointer compaction: read pointer i scans every slot, write pointer k
// advances only on keepers. Returns the new logical length. O(n), O(1).
package main

func RemoveElement(nums []int, val int) int {
	k := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}
