// LC 191. Number of 1 Bits

package main

// hammingWeight counts set bits via Brian Kernighan's loop.
// O(popcount(n)) time, O(1) space.
func hammingWeight(n uint32) int {
	count := 0
	for n != 0 {
		n &= n - 1 // clear the lowest set bit
		count++
	}
	return count
}
