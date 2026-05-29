// LC 3. Longest Substring Without Repeating Characters
package main

// LC 3 (last-index-jump form). The `prev >= l` guard rejects stale
// entries from outside the current window.
func lengthOfLongestSubstring(s string) int {
	last := make(map[byte]int)
	l := 0
	best := 0
	for r := 0; r < len(s); r++ {
		ch := s[r]
		if prev, ok := last[ch]; ok && prev >= l {
			l = prev + 1
		}
		last[ch] = r
		if r-l+1 > best {
			best = r - l + 1
		}
	}
	return best
}
