# LC 25. Reverse Nodes in k-Group
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """LC 25: reverse the linked list in groups of k; trailing run < k stays as-is.

    Iterative, O(n) time, O(1) extra space. The dummy sentinel pins a stable
    handle on the result so the very first group reverses without a special case.
    group_prev is the node directly before the current group; _kth_after peeks
    ahead k nodes to confirm a full group exists before any pointer rewiring;
    if it returns None the suffix is shorter than k and the loop exits.
    """
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = _kth_after(group_prev, k)
        if kth is None:
            break
        group_next = kth.next

        prev: Optional[ListNode] = group_next
        curr: Optional[ListNode] = group_prev.next
        while curr is not group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        new_group_tail = group_prev.next
        group_prev.next = kth
        group_prev = new_group_tail

    return dummy.next


def _kth_after(node: ListNode, k: int) -> Optional[ListNode]:
    """Return the k-th node strictly after `node`, or None if fewer than k nodes exist."""
    curr: Optional[ListNode] = node
    while curr is not None and k > 0:
        curr = curr.next
        k -= 1
    return curr
