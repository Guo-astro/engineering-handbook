// LC 49. Group Anagrams
// Bucket by canonical form. The 26-int character-count signature is O(k)
// per string vs O(k log k) for sorted-string keys. The '#' delimiter
// prevents counts like {1, 11} from colliding with {11, 1}.
// O(N * k) time, O(N * k) space, for N strings of average length k.
package main

import (
	"strconv"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)
	for _, s := range strs {
		var counts [26]int
		for i := 0; i < len(s); i++ {
			counts[s[i]-'a']++
		}
		var sb strings.Builder
		sb.Grow(64)
		for _, c := range counts {
			sb.WriteByte('#')
			sb.WriteString(strconv.Itoa(c))
		}
		key := sb.String()
		// Nil-slice append is safe: missing keys give a zero-value []string
		// that append extends to a singleton.
		groups[key] = append(groups[key], s)
	}
	out := make([][]string, 0, len(groups))
	for _, g := range groups {
		out = append(out, g)
	}
	return out
}
