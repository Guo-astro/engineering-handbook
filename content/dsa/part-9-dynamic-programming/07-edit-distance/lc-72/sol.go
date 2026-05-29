// LC 72. Edit Distance

package main

func minDistance(word1, word2 string) int {
	m, n := len(word1), len(word2)
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 0; i <= m; i++ {
		dp[i][0] = i // i deletes
	}
	for j := 0; j <= n; j++ {
		dp[0][j] = j // j inserts
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1] // match: free diagonal
			} else {
				dp[i][j] = 1 + min3(
					dp[i-1][j-1], // replace
					dp[i-1][j],   // delete from word1
					dp[i][j-1],   // insert into word1
				)
			}
		}
	}
	return dp[m][n]
}

func min3(a, b, c int) int {
	m := a
	if b < m {
		m = b
	}
	if c < m {
		m = c
	}
	return m
}
