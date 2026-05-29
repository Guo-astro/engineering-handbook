// LC 125. Valid Palindrome
// Two pointers converging from the ends, skipping non-alphanumerics, with
// case-folded comparison. ASCII-only per LC constraints, so byte-level
// classification is safe and avoids the unicode package overhead. O(n), O(1).
package main

func isPalindrome(s string) bool {
	isAlnum := func(b byte) bool {
		return (b >= '0' && b <= '9') ||
			(b >= 'a' && b <= 'z') ||
			(b >= 'A' && b <= 'Z')
	}
	toLower := func(b byte) byte {
		if b >= 'A' && b <= 'Z' {
			return b + ('a' - 'A')
		}
		return b
	}
	l, r := 0, len(s)-1
	for l < r {
		for l < r && !isAlnum(s[l]) {
			l++
		}
		for l < r && !isAlnum(s[r]) {
			r--
		}
		if toLower(s[l]) != toLower(s[r]) {
			return false
		}
		l++
		r--
	}
	return true
}
