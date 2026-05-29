// Chapter 7.0 — Recursion patterns: linear, tree, and divide-and-conquer
package main

// Shape 1: linear recursion. Go does NOT eliminate tail calls in general;
// goroutine stacks grow segmentedly from the heap, so depth is bounded by
// available memory, not a fixed limit.
func fibLinear(n int) int64 { return fibLinearAcc(n, 0, 1) }

func fibLinearAcc(n int, a, b int64) int64 {
	if n == 0 {
		return a
	}
	return fibLinearAcc(n-1, b, a+b)
}

// Shape 2: tree recursion. Exponential without memo.
func fibTree(n int) int64 {
	if n < 2 {
		return int64(n)
	}
	return fibTree(n-1) + fibTree(n-2)
}

// Shape 2 + memo.
func fibMemo(n int) int64 {
	cache := make(map[int]int64)
	return fibMemoHelper(n, cache)
}

func fibMemoHelper(n int, cache map[int]int64) int64 {
	if n < 2 {
		return int64(n)
	}
	if v, ok := cache[n]; ok {
		return v
	}
	ans := fibMemoHelper(n-1, cache) + fibMemoHelper(n-2, cache)
	cache[n] = ans
	return ans
}

// Canonical entrypoint.
func fib(n int) int64 { return fibMemo(n) }

// Shape 3: divide-and-conquer. The Go slice-aliasing footgun is sidestepped
// by always allocating a fresh slice in the base case; recursive halves are
// independent views, but the merge step writes into a fresh slice anyway.
func mergeSort(nums []int) []int {
	if len(nums) <= 1 {
		out := make([]int, len(nums))
		copy(out, nums)
		return out
	}
	mid := len(nums) / 2
	left := mergeSort(nums[:mid])
	right := mergeSort(nums[mid:])
	return mergeSlices(left, right)
}

func mergeSlices(a, b []int) []int {
	out := make([]int, 0, len(a)+len(b))
	i, j := 0, 0
	for i < len(a) && j < len(b) {
		if a[i] <= b[j] {
			out = append(out, a[i])
			i++
		} else {
			out = append(out, b[j])
			j++
		}
	}
	out = append(out, a[i:]...)
	out = append(out, b[j:]...)
	return out
}
