// LC 518. Coin Change II
// OUTER loop = coins is mandatory; counts unordered combinations.
package main

func change(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1                              // empty multiset is one valid way
	for _, c := range coins {              // OUTER = coins -> combinations
		for a := c; a <= amount; a++ {
			dp[a] += dp[a-c]
		}
	}
	return dp[amount]
}
