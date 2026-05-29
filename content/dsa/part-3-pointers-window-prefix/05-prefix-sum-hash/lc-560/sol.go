// LC 560. Subarray Sum Equals K
package main

// LC 560.
func subarraySum(nums []int, k int) int {
	counts := map[int64]int{0: 1}
	var prefix int64 = 0
	answer := 0
	kL := int64(k)
	for _, x := range nums {
		prefix += int64(x)
		// comma-ok lookup avoids inserting a zero on miss.
		if c, ok := counts[prefix-kL]; ok {
			answer += c
		}
		counts[prefix]++
	}
	return answer
}
