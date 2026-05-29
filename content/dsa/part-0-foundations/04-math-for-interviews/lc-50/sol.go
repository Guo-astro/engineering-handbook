// LC 50. Pow(x, n)

package main

// myPow computes x^n via binary exponentiation.
// O(log |n|) time, O(1) space.
func myPow(x float64, n int) float64 {
	// Promote to int64: on 32-bit platforms Go's int is int32, where -MinInt32 wraps.
	m := int64(n)
	if m < 0 {
		x = 1.0 / x
		m = -m
	}
	result := 1.0
	base := x
	for m > 0 {
		if m&1 == 1 {
			result *= base
		}
		base *= base
		m >>= 1
	}
	return result
}
