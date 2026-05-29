// LC 28. Find the Index of the First Occurrence in a String
package main

func strStr(haystack, needle string) int {
	n := len(haystack)
	m := len(needle)
	if m == 0 {
		return 0
	}
	if m > n {
		return -1
	}
	for i := 0; i <= n-m; i++ {
		j := 0
		for j < m && haystack[i+j] == needle[j] {
			j++
		}
		if j == m {
			return i
		}
	}
	return -1
}
