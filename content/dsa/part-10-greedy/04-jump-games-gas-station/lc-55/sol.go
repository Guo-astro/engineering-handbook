// LC 55. Jump Game
// five canonical cases under sol_test.
// Greedy max-reach frontier sweep. O(n) time, O(1) space.
package main

func CanJump(nums []int) bool {
	maxReach := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		if i > maxReach {
			return false
		}
		if i+nums[i] > maxReach {
			maxReach = i + nums[i]
		}
		if maxReach >= n-1 {
			return true
		}
	}
	return true
}
