// LC 509. Fibonacci Number
package main

type fibSolver struct {
	memo map[int]int
}

func newFibSolver() *fibSolver {
	return &fibSolver{memo: map[int]int{0: 0, 1: 1}}
}

func (s *fibSolver) fib(n int) int {
	if v, ok := s.memo[n]; ok {
		return v
	}
	v := s.fib(n-1) + s.fib(n-2)
	s.memo[n] = v
	return v
}

// Fib is the entry point. Each call gets a fresh memo so cross-call state
// can never contaminate the result; see the chapter's pitfall on this.
func Fib(n int) int {
	return newFibSolver().fib(n)
}
