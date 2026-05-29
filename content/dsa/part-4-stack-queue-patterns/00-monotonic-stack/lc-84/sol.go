// LC 84. Largest Rectangle in Histogram
package main

func largestRectangleArea(heights []int) int {
	ans := 0
	stack := make([]int, 0, len(heights)) // non-decreasing stack of indices
	n := len(heights)
	for i := 0; i <= n; i++ {
		cur := 0
		if i < n {
			cur = heights[i]
		}
		for len(stack) > 0 && heights[stack[len(stack)-1]] > cur {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			h := heights[top]
			w := i
			if len(stack) > 0 {
				w = i - stack[len(stack)-1] - 1
			}
			if h*w > ans {
				ans = h * w
			}
		}
		stack = append(stack, i)
	}
	return ans
}
