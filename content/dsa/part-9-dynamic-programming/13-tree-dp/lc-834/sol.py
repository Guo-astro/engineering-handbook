# LC 834. Sum of Distances in Tree
# implements the re-rooting
# technique (pattern extension).
"""LC 834. For every node i, the sum of distances to all other nodes.

Naive approach: run BFS from every node, O(n^2). Re-rooting collapses
that to O(n) with two passes:

  Pass 1 (post-order):  for each node, compute count[u] = subtree size
                         (including u) and answer[root] = sum of distances
                         from root to every node in the tree.
  Pass 2 (pre-order):   for each child v of a node u, derive answer[v] from
                         answer[u] in O(1):
                            answer[v] = answer[u] - count[v] + (n - count[v])
                         Intuition: re-root from u to v. The count[v] nodes
                         in v's subtree each get 1 step closer; the
                         (n - count[v]) nodes outside each get 1 step farther.

The graph is given as `edges`; we build an undirected adjacency list once.
"""
import sys
from typing import List


sys.setrecursionlimit(10**6)


def sum_of_distances_in_tree(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]

    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    count = [1] * n     # subtree size (post-order pass)
    answer = [0] * n    # answer[u] = sum of distances from u to all nodes

    # Pass 1: post-order DFS rooted at 0. Compute count[u] and the partial
    # answer[0] = sum of depths from node 0.
    def post(u: int, parent: int) -> None:
        for v in adj[u]:
            if v == parent:
                continue
            post(v, u)
            count[u] += count[v]
            answer[u] += answer[v] + count[v]

    # Pass 2: pre-order DFS. Re-root from u to each child v in O(1).
    def pre(u: int, parent: int) -> None:
        for v in adj[u]:
            if v == parent:
                continue
            answer[v] = answer[u] - count[v] + (n - count[v])
            pre(v, u)

    post(0, -1)
    pre(0, -1)
    return answer
