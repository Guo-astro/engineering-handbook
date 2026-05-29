# LC 684. Redundant Connection
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))  # 1-indexed; parent[0] unused
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        # Path compression (recursive two-pass).
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # already connected; would form a cycle
        # Union by rank: attach shorter tree under taller root.
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """LC 684: return the edge that, if removed, leaves a tree.
    If multiple, return the one occurring last in the input."""
    n = len(edges)  # n nodes, n edges (one extra)
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return []
