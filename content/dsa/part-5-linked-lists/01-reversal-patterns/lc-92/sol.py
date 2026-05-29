# LC 92. Reverse Linked List II
# One-pass head-insertion variant: walk a sentinel (left-1) steps to
# land just before the segment, then for (right-left) iterations splice
# each newly-encountered node to the front of the reversed prefix.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    """One-pass range reversal via head-insertion. Time O(n), space O(1)."""
    if head is None or left == right:
        return head

    dummy = ListNode(0, head)
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next  # type: ignore[assignment]

    # `curr` is the first node of the segment to reverse; it stays put and
    # becomes the segment's tail. Each iteration lifts curr.next out and
    # splices it to the front of the reversed prefix.
    curr = pre.next
    for _ in range(right - left):
        moved = curr.next
        curr.next = moved.next
        moved.next = pre.next
        pre.next = moved

    return dummy.next
