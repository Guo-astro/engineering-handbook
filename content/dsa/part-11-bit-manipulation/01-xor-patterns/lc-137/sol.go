// LC 137. Single Number II
//
// Per-bit count modulo 3: O(32n) = O(n) time, O(1) space.

package main

func singleNumber(nums []int) int {
	var result int32
	for i := 0; i < 32; i++ {
		bitSum := 0
		for _, x := range nums {
			bitSum += (int(int32(x)) >> i) & 1
		}
		if bitSum%3 != 0 {
			result |= 1 << i
		}
	}
	return int(result)
}
