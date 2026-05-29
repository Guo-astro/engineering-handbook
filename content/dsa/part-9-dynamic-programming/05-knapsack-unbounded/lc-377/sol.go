// LC 377. Combination Sum IV
// OUTER loop = amounts; counts ordered sequences.
package main

func combinationSum4(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1                              // empty sequence is one valid way
	for a := 1; a <= target; a++ {         // OUTER = amounts -> permutations
		for _, n := range nums {
			if n <= a {
				dp[a] += dp[a-n]
			}
		}
	}
	return dp[target]
}
