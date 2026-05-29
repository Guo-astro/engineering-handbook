# LC 1372. Longest ZigZag Path in a Binary Tree
"""LC 1372. Return the longest zigzag path length in a binary tree.

Shape 3 of tree DP (the diameter trick), composed with shape 4 (tuple
return). The helper returns a 2-tuple (left_extending, right_extending)
describing how far a zigzag chain entering this node from above can extend
in each direction. A closure-captured global takes the max with the
through-this-node composite at every step. The final answer lives in the
global, NOT in the helper's return value — that split is the chapter's
load-bearing insight.
"""
import sys
from dataclasses import dataclass
from typing import Optional, Tuple


sys.setrecursionlimit(10**6)


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def longest_zig_zag(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    best = 0

    def helper(node: Optional[TreeNode]) -> Tuple[int, int]:
        nonlocal best
        if node is None:
            return (-1, -1)  # sentinel: no chain to extend
        # Each child contributes the chain ending in the OTHER direction:
        # entering me leftward continues the parent's right-extending chain.
        _, left_right = helper(node.left)
        right_left, _ = helper(node.right)
        left_len = left_right + 1
        right_len = right_left + 1
        # Update the global BEFORE building the return tuple, so the
        # left-to-right argument evaluation order in max can never see
        # stale state (see §"Two pitfalls that bite", side-effect ordering).
        local_best = left_len if left_len > right_len else right_len
        if local_best > best:
            best = local_best
        return (left_len, right_len)

    helper(root)
    return best
