// LC 198. House Robber
package main

func rob(nums []int) int {
	prev2, prev1 := 0, 0
	for _, x := range nums {
		cur := prev1
		if prev2+x > cur {
			cur = prev2 + x
		}
		prev2 = prev1
		prev1 = cur
	}
	return prev1
}
