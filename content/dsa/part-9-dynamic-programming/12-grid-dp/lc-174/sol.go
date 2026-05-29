// LC 174. Dungeon Game
// Backward grid DP:
//   dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
// Sentinel padding with math.MaxInt32 so the bottom-right corner falls
// back to its own clamp; iteration is bottom-right to top-left.
package main

import "math"

func calculateMinimumHP(dungeon [][]int) int {
	m := len(dungeon)
	n := len(dungeon[0])
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt32
		}
	}
	dp[m][n-1] = 1
	dp[m-1][n] = 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			need := min2(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
			dp[i][j] = max2(need, 1)
		}
	}
	return dp[0][0]
}

func min2(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max2(a, b int) int {
	if a > b {
		return a
	}
	return b
}
