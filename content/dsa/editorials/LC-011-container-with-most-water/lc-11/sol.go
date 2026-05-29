// LC 11. Container With Most Water
package main

// maxArea implements LC 11 in O(n) using two pointers from opposite ends.
// Each step advances the pointer at the shorter wall; on ties, advance right.
func maxArea(height []int) int {
	left, right := 0, len(height)-1
	best := 0
	for left < right {
		hL, hR := height[left], height[right]
		width := right - left
		if hL < hR {
			if a := hL * width; a > best {
				best = a
			}
			left++
		} else {
			if a := hR * width; a > best {
				best = a
			}
			right--
		}
	}
	return best
}
