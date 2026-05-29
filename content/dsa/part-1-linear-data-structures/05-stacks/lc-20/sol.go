// LC 20. Valid Parentheses
// Push openers; on a closer, peek the top opener and pop iff it matches.
// Keying the pair table by closer keeps the lookup branch-free. The
// terminal stack-empty check rejects unmatched openers.
// Idiomatic Go stack: a slice with append for push and reslice for pop.
// O(n), O(n).
package main

func isValid(s string) bool {
	pair := map[byte]byte{')': '(', ']': '[', '}': '{'}
	stack := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		switch c {
		case '(', '[', '{':
			stack = append(stack, c)
		default:
			if len(stack) == 0 || stack[len(stack)-1] != pair[c] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
