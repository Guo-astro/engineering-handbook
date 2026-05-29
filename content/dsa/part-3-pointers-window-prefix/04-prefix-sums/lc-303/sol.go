// LC 303. Range Sum Query - Immutable
package main

// NumArray (LC 303). Construct in O(n); SumRange in O(1).
type NumArray struct {
	prefix []int64
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	// prefix has length n + 1; prefix[0] = 0 is the empty-sum sentinel.
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(nums[i])
	}
	return NumArray{prefix: prefix}
}

func (na *NumArray) SumRange(left, right int) int {
	return int(na.prefix[right+1] - na.prefix[left])
}
