# LC 206. Reverse Linked List
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """Iterative: prev/curr/next three-pointer rewire.

    Loop invariant on entry: every node strictly to the left of curr has been
    rewired so its next pointer goes one step backward; prev is the new head
    of that already-reversed prefix; the suffix starting at curr is unchanged.
    Time O(n), auxiliary space O(1).
    """
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursive: invert the tail, then rewire head.next.next = head.

    Recursion depth is O(n); CPython's default limit is 1000, so for n > ~900
    the caller must raise sys.setrecursionlimit() or use the iterative form.
    Time O(n), auxiliary space O(n) on the call stack.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
