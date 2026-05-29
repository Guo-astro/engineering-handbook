// Suffix array via prefix doubling, plus Kasai LCP. O(n log^2 n) build, O(n) LCP.
package main

import "sort"

func BuildSuffixArray(s string) []int {
	n := len(s)
	if n == 0 {
		return []int{}
	}
	sa := make([]int, n)
	rank := make([]int, n)
	tmp := make([]int, n)
	for i := 0; i < n; i++ {
		sa[i] = i
		rank[i] = int(s[i])
	}
	k := 1
	key := func(i, kk int) (int, int) {
		var second int
		if i+kk < n {
			second = rank[i+kk]
		} else {
			second = -1
		}
		return rank[i], second
	}
	less := func(a, b, kk int) bool {
		ar, as := key(a, kk)
		br, bs := key(b, kk)
		if ar != br {
			return ar < br
		}
		return as < bs
	}
	equal := func(a, b, kk int) bool {
		ar, as := key(a, kk)
		br, bs := key(b, kk)
		return ar == br && as == bs
	}
	for {
		kk := k
		sort.SliceStable(sa, func(i, j int) bool {
			return less(sa[i], sa[j], kk)
		})
		tmp[sa[0]] = 0
		for j := 1; j < n; j++ {
			tmp[sa[j]] = tmp[sa[j-1]]
			if !equal(sa[j], sa[j-1], kk) {
				tmp[sa[j]]++
			}
		}
		copy(rank, tmp)
		if rank[sa[n-1]] == n-1 {
			break
		}
		k *= 2
	}
	return sa
}

func BuildLcpKasai(s string, sa []int) []int {
	n := len(s)
	if n == 0 {
		return []int{}
	}
	inv := make([]int, n)
	lcp := make([]int, n)
	for i := 0; i < n; i++ {
		inv[sa[i]] = i
	}
	h := 0
	for i := 0; i < n; i++ {
		if inv[i] > 0 {
			j := sa[inv[i]-1]
			for i+h < n && j+h < n && s[i+h] == s[j+h] {
				h++
			}
			lcp[inv[i]] = h
			if h > 0 {
				h--
			}
		} else {
			h = 0
		}
	}
	return lcp
}
