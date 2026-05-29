// LC 1668. Maximum Repeating Substring
package strings12

// ZFunction returns the Z-array of s in O(n). z[0] = 0 by convention.
func ZFunction(s string) []int {
	n := len(s)
	z := make([]int, n)
	l, r := 0, 0
	for i := 1; i < n; i++ {
		if i < r {
			if r-i < z[i-l] {
				z[i] = r - i
			} else {
				z[i] = z[i-l]
			}
		}
		for i+z[i] < n && s[z[i]] == s[i+z[i]] {
			z[i]++
		}
		if i+z[i] > r {
			l = i
			r = i + z[i]
		}
	}
	return z
}

// MaxRepeating returns the largest k such that word^k is a substring of sequence.
func MaxRepeating(sequence, word string) int {
	m := len(word)
	n := len(sequence)
	if m == 0 || m > n {
		return 0
	}
	s := word + "#" + sequence
	z := ZFunction(s)
	best := 0
	for start := 0; start < n; start++ {
		i := m + 1 + start
		run := 0
		for i+m <= len(s) && z[i] >= m {
			run++
			i += m
		}
		if run > best {
			best = run
		}
	}
	return best
}
