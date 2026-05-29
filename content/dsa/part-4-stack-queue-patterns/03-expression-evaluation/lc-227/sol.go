// LC 227. Basic Calculator II
package main

func Calculate(s string) int {
	stack := make([]int, 0, len(s))
	num := 0
	op := byte('+')
	n := len(s)
	for i := 0; i < n; i++ {
		ch := s[i]
		if ch >= '0' && ch <= '9' {
			num = num*10 + int(ch-'0')
		}
		isLast := i == n-1
		isOp := ch != ' ' && !(ch >= '0' && ch <= '9')
		if isOp || isLast {
			switch op {
			case '+':
				stack = append(stack, num)
			case '-':
				stack = append(stack, -num)
			case '*':
				stack[len(stack)-1] *= num
			case '/':
				stack[len(stack)-1] /= num
			}
			num = 0
			op = ch
		}
	}
	total := 0
	for _, v := range stack {
		total += v
	}
	return total
}
