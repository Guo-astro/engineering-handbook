// LC 239. Sliding Window Maximum
package main

// MaxSlidingWindow returns the max over every contiguous window of size k.
// Implemented as a ring buffer over indices, kept monotone-decreasing in
// nums[idx]. Go ships no native deque; container/list has high overhead and
// slice[1:] for popleft is O(n), which would defeat the algorithm. The ring
// buffer is O(1) per push and pop on both ends.
func MaxSlidingWindow(nums []int, k int) []int {
	n := len(nums)
	if n == 0 || k <= 0 {
		return []int{}
	}
	dq := make([]int, n) // dq[head..tail-1] holds monotone-decreasing indices
	head, tail := 0, 0
	out := make([]int, 0, n-k+1)
	for i, x := range nums {
		// Drop the front index if it has fallen out of the window.
		if head < tail && dq[head] <= i-k {
			head++
		}
		// Maintain monotone-decreasing tail.
		for head < tail && nums[dq[tail-1]] <= x {
			tail--
		}
		dq[tail] = i
		tail++
		if i >= k-1 {
			out = append(out, nums[dq[head]])
		}
	}
	return out
}
