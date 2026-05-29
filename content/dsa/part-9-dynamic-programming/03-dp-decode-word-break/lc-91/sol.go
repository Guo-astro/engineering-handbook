// LC 91. Decode Ways

package main

// numDecodings (LC 91): number of ways to decode the digit string s.
func numDecodings(s string) int {
	n := len(s)
	if n == 0 || s[0] == '0' {
		return 0
	}
	// Rolling window: prev2 = dp[i-2], prev1 = dp[i-1].
	prev2, prev1 := 1, 1
	for i := 2; i <= n; i++ {
		cur := 0
		if s[i-1] != '0' {
			cur += prev1
		}
		two := int(s[i-2]-'0')*10 + int(s[i-1]-'0')
		if two >= 10 && two <= 26 {
			cur += prev2
		}
		prev2, prev1 = prev1, cur
	}
	return prev1
}
