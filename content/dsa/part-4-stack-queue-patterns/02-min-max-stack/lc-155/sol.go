// LC 155. Min Stack
package main

// MinStack supports O(1) Push, Pop, Top, GetMin via a parallel mins slice
// pinned to the values slice in lockstep.
type MinStack struct {
	values []int
	mins   []int
}

func NewMinStack() *MinStack { return &MinStack{} }

func (s *MinStack) Push(val int) {
	s.values = append(s.values, val)
	current := val
	if n := len(s.mins); n > 0 && s.mins[n-1] < current {
		current = s.mins[n-1]
	}
	s.mins = append(s.mins, current)
}

func (s *MinStack) Pop() {
	s.values = s.values[:len(s.values)-1]
	s.mins = s.mins[:len(s.mins)-1]
}

func (s *MinStack) Top() int    { return s.values[len(s.values)-1] }
func (s *MinStack) GetMin() int { return s.mins[len(s.mins)-1] }
