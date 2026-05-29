// LC 5. Longest Palindromic Substring
package main

// LongestPalindrome: 2D DP by-length. O(n^2) time, O(n^2) space.
func LongestPalindrome(s string) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	// isPalin[i][j] = true iff s[i..j] is a palindrome.
	isPalin := make([][]bool, n)
	for i := range isPalin {
		isPalin[i] = make([]bool, n)
	}
	start, maxLen := 0, 1

	// Length 1.
	for i := 0; i < n; i++ {
		isPalin[i][i] = true
	}

	// Length 2.
	for i := 0; i+1 < n; i++ {
		if s[i] == s[i+1] {
			isPalin[i][i+1] = true
			start, maxLen = i, 2
		}
	}

	// Length L from 3 to n.
	for L := 3; L <= n; L++ {
		for i := 0; i+L-1 < n; i++ {
			j := i + L - 1
			if s[i] == s[j] && isPalin[i+1][j-1] {
				isPalin[i][j] = true
				if L > maxLen {
					start, maxLen = i, L
				}
			}
		}
	}
	return s[start : start+maxLen]
}

// LongestPalindromeCenters: expand around centers. O(n^2) time, O(1) space.
func LongestPalindromeCenters(s string) string {
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
