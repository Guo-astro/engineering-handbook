# LC 232. Implement Queue using Stacks
from typing import List


class MyQueue:
    """LC 232. FIFO via two LIFO stacks (inbox/outbox), amortized O(1) per op.

    Push always lands on inbox. Pop and peek always read from outbox; when
    outbox is empty they drain inbox into it once, reversing the order so
    the bottom of inbox becomes the top of outbox -- the FIFO front.
    """

    def __init__(self) -> None:
        self.inbox: List[int] = []
        self.outbox: List[int] = []

    def push(self, x: int) -> None:
        self.inbox.append(x)  # O(1) always

    def _transfer(self) -> None:
        # Drain inbox into outbox; only invoked when outbox is empty so the
        # combined "outbox.reversed ++ inbox" FIFO order is preserved.
        while self.inbox:
            self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        if not self.outbox:
            self._transfer()
        return self.outbox.pop()  # O(1) amortized

    def peek(self) -> int:
        if not self.outbox:
            self._transfer()
        return self.outbox[-1]  # O(1) amortized

    def empty(self) -> bool:
        return not self.inbox and not self.outbox
