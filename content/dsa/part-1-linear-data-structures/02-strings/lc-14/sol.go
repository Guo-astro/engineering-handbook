// LC 14. Longest Common Prefix
// Vertical scanning: walk columns of strs[0]; on first mismatch (or running
// off the end of any string), return the prefix up to that column.
// Note: indexing s[i] in Go yields a byte; safe for the LC ASCII constraint.
// O(S) where S = sum of lengths, O(1) extra space.
package main

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	first := strs[0]
	for i := 0; i < len(first); i++ {
		c := first[i]
		for k := 1; k < len(strs); k++ {
			if i >= len(strs[k]) || strs[k][i] != c {
				return first[:i]
			}
		}
	}
	return first
}
