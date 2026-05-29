// LC 189. Rotate Array
// Three-reverse trick: reverse the whole array, then reverse the first k,
// then reverse the rest. Avoids the O(n*k) naive shift. O(n), O(1).
package main

func Rotate(nums []int, k int) {
	n := len(nums)
	if n == 0 {
		return
	}
	k %= n // Tolerate k > n; rotating n is a no-op.
	reverse(nums, 0, n-1)
	reverse(nums, 0, k-1)
	reverse(nums, k, n-1)
}

func reverse(a []int, lo, hi int) {
	for lo < hi {
		a[lo], a[hi] = a[hi], a[lo]
		lo++
		hi--
	}
}
