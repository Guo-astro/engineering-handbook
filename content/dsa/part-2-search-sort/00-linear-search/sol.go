// LC linear search — Knuth Algorithm B (The Art of Computer Programming Vol 3 §6.1).
//
// range over a slice yields (index, value) tuples; this is Go's idiomatic
// shape for the same loop. slices.Index from the Go 1.21+ standard library
// is the production-code equivalent; the explicit loop is what the chapter
// teaches because it is what an interviewer asks you to write.
package main

func linearSearch(nums []int, target int) int {
	for i, x := range nums {
		if x == target {
			return i
		}
	}
	return -1
}
