// LC 704. Binary Search. Exact-match closed-interval template.
// LC 35. Search Insert Position. Lower-bound half-open template.
// LC 278. First Bad Version. Predicate-driven half-open template.

package main

// Search is LC 704: exact-match closed-interval template.
//
// Loop invariant: target, if present, is in nums[lo..hi] (both inclusive).
func Search(nums []int, target int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		// overflow-safe midpoint per Bloch 2006
		mid := lo + (hi-lo)/2
		switch {
		case nums[mid] == target:
			return mid
		case nums[mid] < target:
			lo = mid + 1
		default:
			hi = mid - 1
		}
	}
	return -1
}

// SearchInsert is LC 35: lower-bound (leftmost insertion point), half-open
// [lo, hi). Equivalent shape to sort.SearchInts in the standard library.
func SearchInsert(nums []int, target int) int {
	lo, hi := 0, len(nums)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] < target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

// FirstBadVersion is LC 278: predicate-driven leftmost template on [1, n].
// isBadVersion is the API the judge supplies.
func FirstBadVersion(n int, isBadVersion func(int) bool) int {
	lo, hi := 1, n
	for lo < hi {
		mid := lo + (hi-lo)/2
		if isBadVersion(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
