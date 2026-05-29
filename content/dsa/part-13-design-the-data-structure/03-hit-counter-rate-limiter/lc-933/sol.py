# LC 933. Number of Recent Calls
from collections import deque


class RecentCounter:
    """LC 933 — sliding-window-on-stream, deque of timestamps.

    ping(t) records timestamp t (strictly increasing) and returns the
    count of pings inside the inclusive window [t - 3000, t]. Every
    timestamp is enqueued once and dequeued at most once across all
    calls, so the amortized cost per ping is O(1).
    """

    def __init__(self) -> None:
        self.q: deque[int] = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        # Strict `<`: q[0] == t - 3000 is INSIDE the inclusive window.
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
