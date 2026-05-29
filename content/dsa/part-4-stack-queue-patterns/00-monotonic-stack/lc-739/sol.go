// LC 739. Daily Temperatures
package main

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	answer := make([]int, n)
	stack := make([]int, 0, n) // decreasing stack of indices
	for i := 0; i < n; i++ {
		for len(stack) > 0 && temperatures[stack[len(stack)-1]] < temperatures[i] {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			answer[j] = i - j
		}
		stack = append(stack, i)
	}
	return answer
}
