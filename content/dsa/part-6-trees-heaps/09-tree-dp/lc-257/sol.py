# LC 257. Binary Tree Paths
"""LC 257. Return every root-to-leaf path as a list of "->"-joined strings.

Shape 1 of tree DP: accumulator-on-the-stack. The helper threads a running
path down through a parameter and commits to the closure-captured list at
every leaf. Backtracking on the way up keeps siblings independent.
"""
import sys
from dataclasses import dataclass
from typing import List, Optional


# DSH-04: raise the recursion limit once at module top so that deep tree
# inputs (LC 1372 caps at 50,000 nodes; LC 257's worst case is the same
# skewed-chain shape) don't hit CPython's default 1,000-frame ceiling.
sys.setrecursionlimit(10**6)


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    out: List[str] = []
    if root is None:
        return out

    def walk(node: TreeNode, path: List[str]) -> None:
        path.append(str(node.val))
        if node.left is None and node.right is None:
            out.append("->".join(path))
        else:
            if node.left is not None:
                walk(node.left, path)
            if node.right is not None:
                walk(node.right, path)
        path.pop()  # backtrack so siblings see a clean prefix

    walk(root, [])
    return out
