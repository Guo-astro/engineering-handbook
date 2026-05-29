// LC 912. Sort an Array — heap-sort reference (in-place, O(n log n) worst case)
package main

// HeapSort sorts nums in place and returns it. Worst-case O(n log n) time,
// O(1) auxiliary space.
func HeapSort(nums []int) []int {
	n := len(nums)
	// Phase 1: Floyd's build-max-heap, right-to-left from last internal node.
	for start := n/2 - 1; start >= 0; start-- {
		siftDown(nums, start, n)
	}
	// Phase 2: extract max repeatedly into the sorted suffix.
	for end := n - 1; end > 0; end-- {
		nums[0], nums[end] = nums[end], nums[0]
		siftDown(nums, 0, end)
	}
	return nums
}

func siftDown(a []int, root, end int) {
	for {
		left := 2*root + 1
		if left >= end {
			return
		}
		right := left + 1
		child := left
		if right < end && a[right] > a[left] {
			child = right
		}
		if a[root] >= a[child] {
			return
		}
		a[root], a[child] = a[child], a[root]
		root = child
	}
}
