// LC 354. Russian Doll Envelopes
package main

import "sort"

func LengthOfLis(nums []int) int {
	tails := make([]int, 0, len(nums))
	for _, x := range nums {
		i := sort.SearchInts(tails, x) // bisect_left over a sorted []int
		if i == len(tails) {
			tails = append(tails, x)
		} else {
			tails[i] = x
		}
	}
	return len(tails)
}

func MaxEnvelopes(envelopes [][]int) int {
	if len(envelopes) == 0 {
		return 0
	}
	sort.Slice(envelopes, func(i, j int) bool {
		if envelopes[i][0] != envelopes[j][0] {
			return envelopes[i][0] < envelopes[j][0]
		}
		return envelopes[i][1] > envelopes[j][1] // height DESC on width tie
	})
	heights := make([]int, len(envelopes))
	for i, e := range envelopes {
		heights[i] = e[1]
	}
	return LengthOfLis(heights)
}
