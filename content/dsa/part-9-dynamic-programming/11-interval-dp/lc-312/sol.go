// LC 312. Burst Balloons
package main

// LC 312.
func maxCoins(nums []int) int {
	m := len(nums)
	a := make([]int, m+2)
	a[0], a[m+1] = 1, 1
	for i, v := range nums {
		a[i+1] = v
	}
	n := m + 2
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	// Length-major fill keeps every smaller subproblem ready first.
	for length := 2; length < n; length++ {
		for i := 0; i+length < n; i++ {
			j := i + length
			best := 0
			// k = LAST balloon to burst inside (i, j); its neighbors at
			// pop time are guaranteed to be a[i] and a[j].
			for k := i + 1; k < j; k++ {
				gain := a[i]*a[k]*a[j] + dp[i][k] + dp[k][j]
				if gain > best {
					best = gain
				}
			}
			dp[i][j] = best
		}
	}
	return dp[0][n-1]
}
