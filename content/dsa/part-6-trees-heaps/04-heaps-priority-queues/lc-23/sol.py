# LC 23. Merge k Sorted Lists
# k-way merge with a min-heap of K cursors. Tie-break tuple slot 2 (list index)
# is mandatory: ListNode is unorderable, so the heap must never compare two
# ListNode objects directly.
import heapq
from typing import List, Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, nxt: Optional["ListNode"] = None):
        self.val, self.next = val, nxt


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """O(N log K) where N = total nodes, K = number of lists."""
    heap: list[tuple[int, int, ListNode]] = []
    for i, head in enumerate(lists):
        if head is not None:
            heapq.heappush(heap, (head.val, i, head))

    dummy = ListNode()
    tail = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, i, node.next))
    tail.next = None
    return dummy.next
