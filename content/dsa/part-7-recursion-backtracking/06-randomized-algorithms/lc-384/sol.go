// LC 384. Shuffle an Array
package main

import "math/rand"

type Solution struct {
	original []int
	rng      *rand.Rand
}

func Constructor(nums []int) Solution {
	cp := make([]int, len(nums))
	copy(cp, nums)
	return Solution{
		original: cp,
		rng:      rand.New(rand.NewSource(42)),
	}
}

func (s *Solution) Reset() []int {
	cp := make([]int, len(s.original))
	copy(cp, s.original)
	return cp
}

func (s *Solution) Shuffle() []int {
	arr := make([]int, len(s.original))
	copy(arr, s.original)
	// Durstenfeld: i descends from len(arr)-1 down to 1; rng.Intn(i+1) is
	// uniform on [0, i] inclusive. Go's rand.Shuffle ships with the same loop.
	for i := len(arr) - 1; i > 0; i-- {
		j := s.rng.Intn(i + 1)
		arr[i], arr[j] = arr[j], arr[i]
	}
	return arr
}
