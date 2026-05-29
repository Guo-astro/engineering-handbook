# LC 1046. Last Stone Weight
import heapq


def lastStoneWeight(stones: list[int]) -> int:
    # Python's heapq is a min-heap; negate to get max-heap behavior.
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)  # heaviest
        x = -heapq.heappop(heap)  # second heaviest
        if y != x:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0
