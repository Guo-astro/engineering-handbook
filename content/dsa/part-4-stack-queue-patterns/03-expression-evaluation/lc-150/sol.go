// LC 150. Evaluate Reverse Polish Notation
package main

import "strconv"

func EvalRPN(tokens []string) int {
	stack := make([]int, 0, len(tokens))
	for _, t := range tokens {
		if len(t) == 1 && (t == "+" || t == "-" || t == "*" || t == "/") {
			b := stack[len(stack)-1]
			a := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			switch t {
			case "+":
				stack = append(stack, a+b)
			case "-":
				stack = append(stack, a-b)
			case "*":
				stack = append(stack, a*b)
			case "/":
				// Go integer division truncates toward zero, matching LC 150.
				stack = append(stack, a/b)
			}
		} else {
			n, _ := strconv.Atoi(t)
			stack = append(stack, n)
		}
	}
	return stack[0]
}
