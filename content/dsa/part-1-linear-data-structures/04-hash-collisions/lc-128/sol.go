// LC 128. Longest Consecutive Sequence
// Build a hash set, then for each value, only start an inner walk when
// (x - 1) is absent — i.e., x is the minimum of its run. Each element is
// touched at most twice, giving O(n) total work assuming O(1) average
// set membership. O(n) time, O(n) space.
package main

func longestConsecutive(nums []int) int {
	s := make(map[int]struct{}, len(nums))
	for _, x := range nums {
		s[x] = struct{}{}
	}
	best := 0
	for x := range s {
		if _, ok := s[x-1]; !ok {
			y := x + 1
			for {
				if _, ok := s[y]; !ok {
					break
				}
				y++
			}
			if y-x > best {
				best = y - x
			}
		}
	}
	return best
}
