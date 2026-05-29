// LC 15. 3Sum
package main

import "sort"

// threeSum returns every unique triplet of values summing to zero.
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	out := [][]int{}
	for i := 0; i+2 < n; i++ {
		if nums[i] > 0 {
			break
		}
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		target := -nums[i]
		l, r := i+1, n-1
		for l < r {
			s := nums[l] + nums[r]
			switch {
			case s < target:
				l++
			case s > target:
				r--
			default:
				out = append(out, []int{nums[i], nums[l], nums[r]})
				l++
				r--
				for l < r && nums[l] == nums[l-1] {
					l++
				}
				for l < r && nums[r] == nums[r+1] {
					r--
				}
			}
		}
	}
	return out
}
