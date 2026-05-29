// LC 28. Find the Index of the First Occurrence in a String
package main

func computeLPS(pattern string) []int {
	m := len(pattern)
	lps := make([]int, m)
	length := 0
	i := 1
	for i < m {
		if pattern[i] == pattern[length] {
			length++
			lps[i] = length
			i++
		} else {
			if length != 0 {
				length = lps[length-1]
			} else {
				lps[i] = 0
				i++
			}
		}
	}
	return lps
}

func strStr(haystack, needle string) int {
	if needle == "" {
		return 0
	}
	n, m := len(haystack), len(needle)
	if m > n {
		return -1
	}
	lps := computeLPS(needle)
	i, j := 0, 0
	for i < n {
		if haystack[i] == needle[j] {
			i++
			j++
			if j == m {
				return i - j
			}
		} else {
			if j != 0 {
				j = lps[j-1]
			} else {
				i++
			}
		}
	}
	return -1
}
