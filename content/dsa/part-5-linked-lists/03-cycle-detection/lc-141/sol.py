# LC 141. Linked List Cycle
from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional["ListNode"] = None


def has_cycle(head: Optional[ListNode]) -> bool:
    """LC 141: return True iff the list contains a cycle, else False."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # pointer identity, not value equality
            return True
    return False
