# LC 707. Design Linked List
"""LC 707 Design Linked List, sentinel-driven singly linked list.

The dummy head removes the head-vs-mid case split: every insert and
delete points at a non-null predecessor `prev`, so the wiring is the
same at index 0 and at index k.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


class MyLinkedList:
    def __init__(self) -> None:
        self.dummy: ListNode = ListNode(0)
        self.length: int = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next  # type: ignore[union-attr]
        return curr.val  # type: ignore[union-attr]

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next  # type: ignore[assignment]
        node = ListNode(val, prev.next)
        prev.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next  # type: ignore[assignment]
        prev.next = prev.next.next  # type: ignore[union-attr]
        self.length -= 1
