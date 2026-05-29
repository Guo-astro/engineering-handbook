// LC 622. Design Circular Queue
// Fixed-capacity ring buffer. head and tail advance modulo cap; an explicit
// count distinguishes empty (count == 0) from full (count == cap), which
// pure modular indexing alone cannot. All operations O(1), O(k) space.
package main

type MyCircularQueue struct {
	buf   []int
	cap   int
	head  int
	tail  int
	count int
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{
		buf: make([]int, k),
		cap: k,
	}
}

func (q *MyCircularQueue) EnQueue(value int) bool {
	if q.count == q.cap {
		return false
	}
	q.buf[q.tail] = value
	q.tail = (q.tail + 1) % q.cap
	q.count++
	return true
}

func (q *MyCircularQueue) DeQueue() bool {
	if q.count == 0 {
		return false
	}
	q.head = (q.head + 1) % q.cap
	q.count--
	return true
}

func (q *MyCircularQueue) Front() int {
	if q.count == 0 {
		return -1
	}
	return q.buf[q.head]
}

func (q *MyCircularQueue) Rear() int {
	if q.count == 0 {
		return -1
	}
	// Add cap before mod to keep the result non-negative when tail == 0.
	return q.buf[(q.tail-1+q.cap)%q.cap]
}

func (q *MyCircularQueue) IsEmpty() bool { return q.count == 0 }
func (q *MyCircularQueue) IsFull() bool  { return q.count == q.cap }
