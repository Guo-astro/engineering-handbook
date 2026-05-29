# LC 23. Merge k Sorted Lists
"""Two implementations of LC 23. Same O(N log k) bound, different
constants, different practical considerations.

`merge_k_lists_heap` keeps a min-heap of (val, list_index, node)
triples. Each of N nodes is pushed once and popped once; each heap op
is O(log k). Tiebreak on list_index keeps Python's heapq from comparing
ListNode references.

`merge_k_lists_divide_conquer` pairs lists up and merges in a
balanced binary tree. log k levels, O(N) work per level. Uses LC 21's
iterative merge as the leaf operation. O(log k) recursion stack
(versus O(k) heap memory) and no PriorityQueue dependency.
"""
from __future__ import annotations
import heapq
from typing import List, Optional


class ListNode:
    """LeetCode's standard singly-linked list node."""

    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def _merge_two(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """The LC 21 iterative merge. Used as the leaf step of the d-and-c form."""
    dummy = ListNode(0)
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next


def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Min-heap of cursors. O(N log k) time, O(k) auxiliary."""
    dummy = ListNode(0)
    tail = dummy
    heap: list = []
    for i, head in enumerate(lists):
        if head is not None:
            heapq.heappush(heap, (head.val, i, head))   # (val, idx, node) tuple.
    while heap:
        _val, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    tail.next = None    # detach any tail still referencing the input.
    return dummy.next


def merge_k_lists_divide_conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Pairwise merge tree. O(N log k) time, O(log k) recursion-stack space."""
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            a = lists[i]
            b = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(_merge_two(a, b))
        lists = merged
    return lists[0]
