// LC 3. Longest Substring Without Repeating Characters
package main

// lengthOfLongestSubstring implements LC 3 in O(n) using a last-index map
// keyed by byte (the ASCII constraint guarantees the array form is safe).
func lengthOfLongestSubstring(s string) int {
	var lastIndex [128]int
	for i := range lastIndex {
		lastIndex[i] = -1
	}
	l, best := 0, 0
	for r := 0; r < len(s); r++ {
		c := s[r]
		if lastIndex[c] >= l {
			l = int(lastIndex[c]) + 1
		}
		lastIndex[c] = r
		if r-l+1 > best {
			best = r - l + 1
		}
	}
	return best
}
