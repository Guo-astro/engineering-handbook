// LC 274. H-Index (counting sort with cap-at-n)
package main

// countingSort is a stable counting sort over bounded integer keys.
// Time: O(n + k) where k = max - min + 1.
// Space: O(n + k).
// Stability comes from the back-to-front scatter with decrement-before-write.
func countingSort(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	lo, hi := nums[0], nums[0]
	for _, x := range nums {
		if x < lo {
			lo = x
		}
		if x > hi {
			hi = x
		}
	}
	k := hi - lo + 1
	count := make([]int, k)
	for _, x := range nums {
		count[x-lo]++
	}
	for i := 1; i < k; i++ {
		count[i] += count[i-1]
	}
	out := make([]int, len(nums))
	for i := len(nums) - 1; i >= 0; i-- {
		x := nums[i]
		count[x-lo]--
		out[count[x-lo]] = x
	}
	return out
}

// hIndex implements LC 274 via counting sort with the cap-at-n trick.
// The answer cannot exceed n, so capping each citation at n collapses
// the universe to [0, n]; counting sort runs in O(n) time and space.
func hIndex(citations []int) int {
	n := len(citations)
	count := make([]int, n+1)
	for _, c := range citations {
		k := c
		if k > n {
			k = n
		}
		count[k]++
	}
	total := 0
	for h := n; h >= 0; h-- {
		total += count[h]
		if total >= h {
			return h
		}
	}
	return 0
}
