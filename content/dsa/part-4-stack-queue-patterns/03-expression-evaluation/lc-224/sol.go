// LC 224. Basic Calculator
package main

func Calculate(s string) int {
	stack := make([]int, 0, 16)
	result, num, sign := 0, 0, 1
	for i := 0; i < len(s); i++ {
		ch := s[i]
		switch {
		case ch >= '0' && ch <= '9':
			num = num*10 + int(ch-'0')
		case ch == '+':
			result += sign * num
			num = 0
			sign = 1
		case ch == '-':
			result += sign * num
			num = 0
			sign = -1
		case ch == '(':
			stack = append(stack, result, sign)
			result = 0
			sign = 1
		case ch == ')':
			result += sign * num
			num = 0
			savedSign := stack[len(stack)-1]
			savedResult := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			result *= savedSign
			result += savedResult
		}
	}
	result += sign * num
	return result
}
