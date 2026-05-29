// Chapter 0.2 — The recursion mental model
// Worked example: factorial(n) by direct recursion.
package main

// Factorial returns n! computed by direct recursion. Panics on n < 0.
func Factorial(n int) int64 {
	if n < 0 {
		panic("factorial is undefined for n < 0")
	}
	// Base case: 0! = 1 by definition. The recursion terminates here.
	if n == 0 {
		return 1
	}
	// Recursive case: n! = n * (n-1)!
	return int64(n) * Factorial(n-1)
}
