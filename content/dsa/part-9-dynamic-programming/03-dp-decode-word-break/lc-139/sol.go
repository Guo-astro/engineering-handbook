// LC 139. Word Break

package main

// wordBreak (LC 139): can s be segmented into words from wordDict.
func wordBreak(s string, wordDict []string) bool {
	n := len(s)
	words := make(map[string]struct{}, len(wordDict))
	maxW := 0
	for _, w := range wordDict {
		words[w] = struct{}{}
		if len(w) > maxW {
			maxW = len(w)
		}
	}
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		lo := i - maxW
		if lo < 0 {
			lo = 0
		}
		for j := lo; j < i; j++ {
			if dp[j] {
				if _, ok := words[s[j:i]]; ok {
					dp[i] = true
					break
				}
			}
		}
	}
	return dp[n]
}
