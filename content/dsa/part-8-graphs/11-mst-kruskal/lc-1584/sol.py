# LC 1584. Min Cost to Connect All Points
from typing import List


class DSU:
    """Disjoint-set with path halving + union by rank."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def min_cost_connect_points(points: List[List[int]]) -> int:
    """LC 1584. Manhattan-distance MST via Kruskal."""
    n = len(points)
    if n <= 1:
        return 0
    edges = []
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            edges.append((abs(xi - xj) + abs(yi - yj), i, j))
    edges.sort()
    dsu = DSU(n)
    total = accepted = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            total += w
            accepted += 1
            if accepted == n - 1:
                break
    return total
