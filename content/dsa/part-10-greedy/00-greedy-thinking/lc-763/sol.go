// LC 763. Partition Labels
package main

func partitionLabels(s string) []int {
	// last[c]: rightmost index at which character c appears.
	last := [26]int{}
	for i := 0; i < len(s); i++ {
		last[s[i]-'a'] = i
	}
	parts := []int{}
	start, end := 0, 0
	for i := 0; i < len(s); i++ {
		// Greedy step: extend the right boundary to the farthest
		// last-occurrence among characters in the current window.
		if last[s[i]-'a'] > end {
			end = last[s[i]-'a']
		}
		if i == end {
			parts = append(parts, end-start+1)
			start = i + 1
		}
	}
	return parts
}
