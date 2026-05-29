# LC 787. Cheapest Flights Within K Stops
"""LC 787: Bellman-Ford with K+1 relaxation passes."""
from typing import List
import math


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """Cheapest src->dst path using at most k stops (k+1 edges).

    Each pass reads from `snapshot` (the previous-pass dist) and writes to
    `dist`. Without that double buffer, a single pass could relax a chain
    src -> a -> b in one iteration of the outer loop, silently violating
    the K-edge bound.
    """
    INF = math.inf
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        snapshot = dist[:]  # CRITICAL: read from previous pass, write to current
        for u, v, w in flights:
            if snapshot[u] == INF:
                continue
            if snapshot[u] + w < dist[v]:
                dist[v] = snapshot[u] + w
    return -1 if dist[dst] == INF else int(dist[dst])
