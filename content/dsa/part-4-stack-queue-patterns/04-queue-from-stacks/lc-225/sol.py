# LC 225. Implement Stack using Queues
# the research doc verified 4 languages for LC 232 only and the LC 225
# inversion is treated as a teaching aside in the chapter prose.
from collections import deque


class MyStack:
    """LC 225. LIFO via a single FIFO queue with a rotation-on-push trick.

    push: enqueue x at the back, then rotate the queue size-1 times so x
    lands at the front. Push is O(n); pop and top are O(1) reads of the
    front. This is the canonical compact answer; the two-queue variant
    trades an extra queue's worth of storage for cheap push and O(n) pop.
    """

    def __init__(self) -> None:
        self.q: deque[int] = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate so the just-pushed element lands at the front.
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()  # O(1)

    def top(self) -> int:
        return self.q[0]  # O(1)

    def empty(self) -> bool:
        return not self.q
