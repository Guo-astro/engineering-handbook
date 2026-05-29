// LC 416. Partition Equal Subset Sum
package main

func canPartition(nums []int) bool {
    total := 0
    for _, x := range nums {
        total += x
    }
    if total&1 == 1 {
        return false
    }
    target := total / 2

    // dp[j] is true iff some subset of seen items sums exactly to j.
    dp := make([]bool, target+1)
    dp[0] = true

    for _, x := range nums {
        // Right-to-left so each item contributes at most once.
        for j := target; j >= x; j-- {
            if dp[j-x] {
                dp[j] = true
            }
        }
        if dp[target] {
            return true
        }
    }
    return dp[target]
}
