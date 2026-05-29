# LC 622. Design Circular Queue
# Fixed-capacity ring buffer. head and tail advance modulo cap; an explicit
# count distinguishes empty (count == 0) from full (count == cap), which
# pure modular indexing alone cannot. All operations O(1), O(k) space.
class MyCircularQueue:
    def __init__(self, k: int):
        self._buf = [0] * k
        self._cap = k
        self._head = 0
        self._tail = 0
        self._count = 0

    def enQueue(self, value: int) -> bool:
        if self._count == self._cap:
            return False
        self._buf[self._tail] = value
        self._tail = (self._tail + 1) % self._cap
        self._count += 1
        return True

    def deQueue(self) -> bool:
        if self._count == 0:
            return False
        self._head = (self._head + 1) % self._cap
        self._count -= 1
        return True

    def Front(self) -> int:
        if self._count == 0:
            return -1
        return self._buf[self._head]

    def Rear(self) -> int:
        if self._count == 0:
            return -1
        # Python's % is non-negative for positive cap, so (tail - 1) % cap
        # wraps correctly when tail == 0.
        return self._buf[(self._tail - 1) % self._cap]

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._cap
