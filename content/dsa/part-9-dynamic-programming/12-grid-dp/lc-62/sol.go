// LC 62. Unique Paths
package main

// UniquePaths2d fills the full m x n table.
func UniquePaths2d(m, n int) int {
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for j := 0; j < n; j++ {
		dp[0][j] = 1
	}
	for i := 0; i < m; i++ {
		dp[i][0] = 1
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}
	return dp[m-1][n-1]
}

// UniquePaths1d uses a rolling row for O(min(m, n)) space.
func UniquePaths1d(m, n int) int {
	if m < n {
		m, n = n, m
	}
	dp := make([]int, n)
	for j := 0; j < n; j++ {
		dp[j] = 1
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[j] = dp[j] + dp[j-1]
		}
	}
	return dp[n-1]
}

// uniquePaths is the LeetCode-shaped public entry point.
func uniquePaths(m, n int) int {
	return UniquePaths2d(m, n)
}
