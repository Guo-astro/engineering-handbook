// LC 213. House Robber II
package main

// Rob solves LC 213 House Robber II.
// Circular case reduces to two linear sub-ranges; take the max.
func Rob(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    if n == 1 {
        return nums[0]
    }
    if n == 2 {
        return maxInt(nums[0], nums[1])
    }
    return maxInt(robLinear(nums[:n-1]), robLinear(nums[1:]))
}

// robLinear is House Robber I via rolling-pair tabulation, O(1) space.
// Recurrence: dp[i] = max(dp[i-1], dp[i-2] + houses[i]).
func robLinear(houses []int) int {
    prev2, prev1 := 0, 0
    for _, x := range houses {
        curr := maxInt(prev1, prev2+x)
        prev2 = prev1
        prev1 = curr
    }
    return prev1
}

func maxInt(a, b int) int {
    if a > b {
        return a
    }
    return b
}
