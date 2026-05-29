# LC 142. Linked List Cycle II
from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional["ListNode"] = None


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """LC 142: return the node where the cycle begins, or None if no cycle."""
    slow = head
    fast = head
    # Phase 1: detect cycle existence.
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # pointer identity, not value equality
            # Phase 2: locate cycle entry. Reset slow; advance both at speed 1.
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
