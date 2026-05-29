# LC 1042. Flower Planting With No Adjacent
# NOT a 2-coloring: 4 flower types over a max-degree-3 graph.
# Greedy single pass works (Brooks' theorem: chromatic number <= Delta
# for non-complete-non-odd-cycle graphs; here Delta = 3, 4 colors suffice).
from typing import List


def garden_no_adj(n: int, paths: List[List[int]]) -> List[int]:
    """LC 1042 — assign each garden one of 4 flower types such that no
    two gardens connected by a path share a type. Max 3 paths per garden,
    so 4 types always suffice (greedy works)."""
    graph = [[] for _ in range(n + 1)]              # 1-indexed
    for x, y in paths:
        graph[x].append(y)
        graph[y].append(x)

    answer = [0] * (n + 1)                          # 0 = unassigned; flowers are 1..4
    for u in range(1, n + 1):
        used = {answer[v] for v in graph[u]}        # types already on neighbors
        for flower in (1, 2, 3, 4):
            if flower not in used:
                answer[u] = flower
                break
    return answer[1:]                               # drop unused index 0
