// LC 707. Design Linked List
// Sentinel-driven singly linked list. The dummy head removes the
// head-vs-mid case split: every insert and delete points at a
// non-null predecessor `prev`, so the wiring is the same at index 0
// and at index k.
package main

type listNode struct {
	val  int
	next *listNode
}

type MyLinkedList struct {
	dummy  *listNode
	length int
}

func Constructor() MyLinkedList {
	return MyLinkedList{dummy: &listNode{}, length: 0}
}

func (l *MyLinkedList) Get(index int) int {
	if index < 0 || index >= l.length {
		return -1
	}
	curr := l.dummy.next
	for i := 0; i < index; i++ {
		curr = curr.next
	}
	return curr.val
}

func (l *MyLinkedList) AddAtHead(val int) { l.AddAtIndex(0, val) }
func (l *MyLinkedList) AddAtTail(val int) { l.AddAtIndex(l.length, val) }

func (l *MyLinkedList) AddAtIndex(index, val int) {
	if index < 0 || index > l.length {
		return
	}
	prev := l.dummy
	for i := 0; i < index; i++ {
		prev = prev.next
	}
	node := &listNode{val: val, next: prev.next}
	prev.next = node
	l.length++
}

func (l *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= l.length {
		return
	}
	prev := l.dummy
	for i := 0; i < index; i++ {
		prev = prev.next
	}
	prev.next = prev.next.next
	l.length--
}
