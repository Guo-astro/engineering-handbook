# LC 215. Kth Largest Element in an Array
# heap solution mirrors
# top-K idiom (min-heap of size k, evict on overflow). Quickselect is the
# primary algorithm at chapter 2.7; this is the heap alternative.
import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """Return the k-th largest element. Min-heap of size k; root is the answer.

    Time:  O(n log k) average and worst case.
    Space: O(k).
    """
    heap: list[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)        # one-shot pop-then-push
    return heap[0]
