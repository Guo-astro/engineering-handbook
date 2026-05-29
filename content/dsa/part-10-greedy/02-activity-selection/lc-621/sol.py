# LC 621. Task Scheduler
from collections import Counter, deque
import heapq


def least_interval(tasks, n):
    """LC 621 Task Scheduler: minimum CPU intervals to finish all tasks
    with cooldown n between identical tasks."""
    if n == 0:
        return len(tasks)
    counts = Counter(tasks)
    # Python heapq is a min-heap; negate counts for max-heap behavior.
    heap = [-c for c in counts.values()]
    heapq.heapify(heap)
    cooldown = deque()  # (negated_count_remaining, ready_time)
    time = 0
    while heap or cooldown:
        time += 1
        if heap:
            neg_c = heapq.heappop(heap)
            remaining = -neg_c - 1
            if remaining > 0:
                cooldown.append((-remaining, time + n))
        if cooldown and cooldown[0][1] == time:
            ready_neg, _ = cooldown.popleft()
            heapq.heappush(heap, ready_neg)
    return time
