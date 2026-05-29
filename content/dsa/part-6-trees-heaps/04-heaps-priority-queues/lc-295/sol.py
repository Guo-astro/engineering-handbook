# LC 295. Find Median from Data Stream
# Two-heap technique: lower half as max-heap (negated); upper half as min-heap.
import heapq


class MedianFinder:
    """Invariant: 0 <= len(lower) - len(upper) <= 1; -lower[0] <= upper[0]."""

    def __init__(self) -> None:
        self.lower: list[int] = []   # max-heap, store as -value
        self.upper: list[int] = []   # min-heap

    def addNum(self, num: int) -> None:
        # Push then rotate: place into lower, then move lower's top to upper.
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))
        # Restore size invariant: lower may carry one extra.
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0
