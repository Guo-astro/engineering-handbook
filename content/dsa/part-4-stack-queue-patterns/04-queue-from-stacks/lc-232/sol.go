// LC 232. Implement Queue using Stacks
//
// Go has no native stack; the canonical idiom is a slice with append for
// push and s = s[:len(s)-1] for pop, both amortized O(1). Both inbox and
// outbox push and pop at the tail, so the slice-as-queue front-pop footgun
// (which is the whole reason LC 232 is interesting in Go) does not apply.
package main

type MyQueue struct {
	inbox  []int
	outbox []int
}

func Constructor() MyQueue { return MyQueue{} }

func (q *MyQueue) Push(x int) {
	q.inbox = append(q.inbox, x) // O(1) amortized
}

func (q *MyQueue) transfer() {
	for n := len(q.inbox); n > 0; n = len(q.inbox) {
		q.outbox = append(q.outbox, q.inbox[n-1])
		q.inbox = q.inbox[:n-1]
	}
}

func (q *MyQueue) Pop() int {
	if len(q.outbox) == 0 {
		q.transfer()
	}
	n := len(q.outbox)
	v := q.outbox[n-1]
	q.outbox = q.outbox[:n-1]
	return v
}

func (q *MyQueue) Peek() int {
	if len(q.outbox) == 0 {
		q.transfer()
	}
	return q.outbox[len(q.outbox)-1]
}

func (q *MyQueue) Empty() bool {
	return len(q.inbox) == 0 && len(q.outbox) == 0
}
