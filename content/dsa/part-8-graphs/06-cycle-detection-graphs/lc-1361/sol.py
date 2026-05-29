# LC 1361. Validate Binary Tree Nodes
"""LC 1361. Each node has 0, 1, or 2 children given by leftChild[i] / rightChild[i]
(value -1 means no child). Return True iff the n nodes form a valid binary tree.

A valid binary tree on n nodes:
  1. exactly one root (in-degree 0); every other node has in-degree 1
  2. no cycle (BFS from root visits every node at most once)
  3. one connected component (BFS from root visits all n nodes)

Conditions 2 and 3 collapse into "BFS from the unique root visits exactly n
distinct nodes". The chapter teaches this as the canonical undirected-DFS
application; the directed framing here is structurally identical because
each edge is parent->child and the parent-tracking guard is replaced by the
"in-degree ≤ 1" precondition.
"""

from typing import List
from collections import deque


def validate_binary_tree_nodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    in_degree = [0] * n
    for c in leftChild:
        if c != -1:
            in_degree[c] += 1
    for c in rightChild:
        if c != -1:
            in_degree[c] += 1

    # exactly one root
    root = -1
    for i in range(n):
        if in_degree[i] == 0:
            if root != -1:
                return False
            root = i
        elif in_degree[i] > 1:
            return False
    if root == -1:
        return False

    # BFS from root; every node must be visited exactly once
    seen = [False] * n
    seen[root] = True
    visited_count = 1
    q = deque([root])
    while q:
        u = q.popleft()
        for v in (leftChild[u], rightChild[u]):
            if v == -1:
                continue
            if seen[v]:           # cycle witness
                return False
            seen[v] = True
            visited_count += 1
            q.append(v)
    return visited_count == n
