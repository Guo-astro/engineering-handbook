// LC 643. Maximum Average Subarray I
package main

// FindMaxAverage solves LC 643. int64 sum absorbs the build phase even when
// k is up to 10^5; postpone the float division to one rounding step at the end.
func FindMaxAverage(nums []int, k int) float64 {
	var windowSum int64 = 0
	for i := 0; i < k; i++ {
		windowSum += int64(nums[i])
	}
	bestSum := windowSum
	for r := k; r < len(nums); r++ {
		windowSum += int64(nums[r]) - int64(nums[r-k])
		if windowSum > bestSum {
			bestSum = windowSum
		}
	}
	return float64(bestSum) / float64(k)
}
