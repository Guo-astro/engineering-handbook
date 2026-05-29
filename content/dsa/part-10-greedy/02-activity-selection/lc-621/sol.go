// LC 621. Task Scheduler
package main

import "container/heap"

type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func leastInterval(tasks []byte, n int) int {
	if n == 0 {
		return len(tasks)
	}
	var counts [26]int
	for _, t := range tasks {
		counts[t-'A']++
	}
	h := &maxHeap{}
	for _, c := range counts {
		if c > 0 {
			heap.Push(h, c)
		}
	}
	type pair struct{ count, ready int }
	cooldown := make([]pair, 0, 26)
	time := 0
	for h.Len() > 0 || len(cooldown) > 0 {
		time++
		if h.Len() > 0 {
			remaining := heap.Pop(h).(int) - 1
			if remaining > 0 {
				cooldown = append(cooldown, pair{remaining, time + n})
			}
		}
		if len(cooldown) > 0 && cooldown[0].ready == time {
			heap.Push(h, cooldown[0].count)
			cooldown = cooldown[1:]
		}
	}
	return time
}
