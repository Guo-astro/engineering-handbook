# LC 743. Network Delay Time
import heapq
from typing import List


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """LC 743. Min time for all nodes to receive signal from k, or -1."""
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append((v, w))

    INF = float("inf")
    dist = [INF] * (n + 1)
    dist[k] = 0

    # Lazy-deletion priority queue: stale entries filtered when popped.
    pq = [(0, k)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue                   # u already settled with smaller dist
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    longest = max(dist[1:])            # 1-indexed nodes
    return -1 if longest == INF else longest
