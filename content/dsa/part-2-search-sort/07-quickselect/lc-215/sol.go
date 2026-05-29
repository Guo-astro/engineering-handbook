// LC 215. Kth Largest Element in an Array
package main

import "math/rand"

func findKthLargest(nums []int, k int) int {
	target := len(nums) - k
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		pivotIdx := partition(nums, lo, hi)
		if pivotIdx == target {
			return nums[pivotIdx]
		}
		if pivotIdx < target {
			lo = pivotIdx + 1
		} else {
			hi = pivotIdx - 1
		}
	}
	return -1 // unreachable for valid input
}

func partition(nums []int, lo, hi int) int {
	randIdx := lo + rand.Intn(hi-lo+1)
	nums[randIdx], nums[hi] = nums[hi], nums[randIdx]
	pivot := nums[hi]
	store := lo
	for i := lo; i < hi; i++ {
		if nums[i] < pivot {
			nums[store], nums[i] = nums[i], nums[store]
			store++
		}
	}
	nums[store], nums[hi] = nums[hi], nums[store]
	return store
}
