// LC 242. Valid Anagram
// Increment-decrement-and-check: build a counter from s, then walk t
// decrementing; any underflow means t is not a permutation of s.
// Length short-circuit avoids building the counter when sizes differ.
// O(n), O(k) where k is the alphabet size.
package main

func isAnagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}
	counts := make(map[byte]int, len(s))
	for i := 0; i < len(s); i++ {
		counts[s[i]]++
	}
	for i := 0; i < len(t); i++ {
		c, ok := counts[t[i]]
		if !ok || c == 0 {
			return false
		}
		counts[t[i]] = c - 1
	}
	return true
}
