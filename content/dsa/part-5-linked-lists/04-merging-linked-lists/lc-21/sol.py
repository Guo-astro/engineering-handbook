# LC 21. Merge Two Sorted Lists
"""Two implementations of LC 21:

`merge_two_lists_iterative` is the chapter's preferred form: dummy node
plus a tail pointer, splice the smaller head, advance that cursor, drain
the survivor in one pointer assignment. O(n + m) time, O(1) auxiliary.

`merge_two_lists_recursive` is the textbook recursive form. Same time
bound, but O(n + m) recursion-stack space; the iterative form is what
ships in interviews.
"""
from __future__ import annotations
from typing import Optional


class ListNode:
    """LeetCode's standard singly-linked list node."""

    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def merge_two_lists_iterative(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Iterative dummy-node + tail-pointer merge. Stable: l1 wins on ties."""
    dummy = ListNode(0)             # sentinel; never returned, .next is the answer.
    tail = dummy                    # invariant: tail points to the last spliced node.
    a, b = l1, l2
    while a is not None and b is not None:
        if a.val <= b.val:          # `<=` keeps the merge stable: l1 wins on tie.
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b   # one O(1) splice drains the survivor.
    return dummy.next


def merge_two_lists_recursive(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Textbook recursive form. O(n + m) recursion stack; prefer iterative."""
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    l2.next = merge_two_lists_recursive(l1, l2.next)
    return l2
