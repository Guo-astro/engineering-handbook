// LC 28. Find the Index of the First Occurrence in a String
package main

func strStr(haystack, needle string) int {
	n, m := len(haystack), len(needle)
	if m == 0 {
		return 0
	}
	if m > n {
		return -1
	}

	const base uint64 = 256
	const mod uint64 = 1_000_000_007

	var highPower uint64 = 1
	for i := 0; i < m-1; i++ {
		highPower = (highPower * base) % mod
	}

	var needleHash, windowHash uint64
	for i := 0; i < m; i++ {
		needleHash = (needleHash*base + uint64(needle[i])) % mod
		windowHash = (windowHash*base + uint64(haystack[i])) % mod
	}

	for i := 0; i <= n-m; i++ {
		if windowHash == needleHash && haystack[i:i+m] == needle {
			return i
		}
		if i < n-m {
			leading := (uint64(haystack[i]) * highPower) % mod
			windowHash = (windowHash + mod - leading) % mod
			windowHash = (windowHash*base + uint64(haystack[i+m])) % mod
		}
	}
	return -1
}
