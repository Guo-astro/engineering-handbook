# LC 990. Satisfiability of Equality Equations
# Two-pass: first union all '==' equations; then for each '!=', check the
# two endpoints have different roots. If any '!=' has equal roots, return False.
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def equations_possible(equations: List[str]) -> bool:
    """LC 990: return True iff the equations can be simultaneously satisfied."""
    dsu = DSU(26)  # 26 lowercase letters as node ids
    # Pass 1: unify all variables connected by '=='.
    for eq in equations:
        if eq[1] == "=":
            dsu.union(ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a"))
    # Pass 2: every '!=' must have endpoints in different sets.
    for eq in equations:
        if eq[1] == "!":
            if dsu.find(ord(eq[0]) - ord("a")) == dsu.find(ord(eq[3]) - ord("a")):
                return False
    return True
