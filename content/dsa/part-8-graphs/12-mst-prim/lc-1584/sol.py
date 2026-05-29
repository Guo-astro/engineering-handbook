# LC 1584. Min Cost to Connect All Points
import heapq
from typing import List


def min_cost_connect_points(points: List[List[int]]) -> int:
    """LC 1584 - Manhattan-distance MST via lazy Prim."""
    n = len(points)
    if n <= 1:
        return 0
    in_mst = [False] * n
    pq: list[tuple[int, int]] = [(0, 0)]   # (weight, vertex)
    total = 0
    edges_added = 0
    while pq and edges_added < n:
        w, u = heapq.heappop(pq)
        if in_mst[u]:
            continue                        # stale entry
        in_mst[u] = True
        total += w
        edges_added += 1
        for v in range(n):
            if not in_mst[v]:
                d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(pq, (d, v))
    return total
