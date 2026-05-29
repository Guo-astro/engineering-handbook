// LC 344. Reverse String
// Two-pointer in-place swap. Go strings are immutable, so the LC signature
// uses []byte for in-place work. O(n), O(1).
package main

func reverseString(s []byte) {
	l, r := 0, len(s)-1
	for l < r {
		s[l], s[r] = s[r], s[l]
		l++
		r--
	}
}
