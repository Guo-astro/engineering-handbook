// LC 260. Single Number III
//
// XOR all -> xor_all = a ^ b. Bucket by lowest differing bit. Two LC-136s.

package main

func singleNumber(nums []int) []int {
	xorAll := int32(0)
	for _, x := range nums {
		xorAll ^= int32(x)
	}
	// int32 negation on MinInt32 wraps to itself; the lowest-set-bit
	// idiom still produces the sign bit alone, which is correct.
	diffBit := xorAll & -xorAll
	var a, b int32
	for _, x := range nums {
		if int32(x)&diffBit != 0 {
			a ^= int32(x)
		} else {
			b ^= int32(x)
		}
	}
	return []int{int(a), int(b)}
}
