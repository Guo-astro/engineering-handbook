// LC 338. Counting Bits

package main

func countBits(n int) []int {
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = dp[i&(i-1)] + 1
	}
	return dp
}
