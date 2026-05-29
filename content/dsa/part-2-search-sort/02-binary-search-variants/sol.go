// LC 33, LC 153, LC 162 plus lower_bound / upper_bound on sorted arrays
// with duplicates, plus binary search on the answer (parametric search).
//
package main

// LowerBound: smallest index i with nums[i] >= target, or len(nums) if none.
func LowerBound(nums []int, target int) int {
	lo, hi := 0, len(nums) // half-open [lo, hi)
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

// UpperBound: smallest index i with nums[i] > target, or len(nums) if none.
func UpperBound(nums []int, target int) int {
	lo, hi := 0, len(nums)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] <= target { // <= flips equality
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

// SearchRotated: LC 33. Exact match in a rotated sorted array (distinct values).
func SearchRotated(nums []int, target int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := lo + (hi-lo)/2 // overflow-safe
		if nums[mid] == target {
			return mid
		}
		if nums[lo] <= nums[mid] {
			// left half [lo..mid] is sorted
			if nums[lo] <= target && target < nums[mid] {
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		} else {
			// right half [mid..hi] is sorted
			if nums[mid] < target && target <= nums[hi] {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
	}
	return -1
}

// FindMinRotated: LC 153.
func FindMinRotated(nums []int) int {
	lo, hi := 0, len(nums)-1
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] > nums[hi] {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return nums[lo]
}

// FindPeakElement: LC 162.
func FindPeakElement(nums []int) int {
	lo, hi := 0, len(nums)-1
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] > nums[mid+1] {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

// BSOnAnswerMin: forward-ref to Part 9. Smallest X in [lo, hi] with
// feasible(X) true; hi + 1 if none.
func BSOnAnswerMin(lo, hi int, feasible func(int) bool) int {
	l, r := lo, hi
	for l < r {
		mid := l + (r-l)/2
		if feasible(mid) {
			r = mid
		} else {
			l = mid + 1
		}
	}
	if feasible(l) {
		return l
	}
	return hi + 1
}
