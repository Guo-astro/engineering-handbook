// LC 5. Longest Palindromic Substring
package main

// longestPalindrome implements LC 5 by expanding around each of the 2n-1
// candidate centers; O(n^2) time, O(1) extra space.
func longestPalindrome(s string) string {
	if len(s) == 0 {
		return ""
	}
	bestL, bestR := 0, 0
	for i := 0; i < len(s); i++ {
		l1, r1 := expand(s, i, i)
		l2, r2 := expand(s, i, i+1)
		if r1-l1 > bestR-bestL {
			bestL, bestR = l1, r1
		}
		if r2-l2 > bestR-bestL {
			bestL, bestR = l2, r2
		}
	}
	return s[bestL : bestR+1]
}

func expand(s string, left, right int) (int, int) {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	return left + 1, right - 1
}
