# LC 124. Binary Tree Maximum Path Sum
"""LC 124. Maximum sum of any non-empty path in a binary tree.

The dual-quantity split is the chapter's central move:
  - RETURN to caller: best straight-down path ending at this node, extending
    into AT MOST one subtree (the parent will glue this into its own path).
  - COMPARE to global: best bent path THROUGH this node, using BOTH subtrees
    (a bent path cannot be extended further upward).
The clamp `max(child_gain, 0)` is the optimization, not a bug fix: if
including a subtree lowers the path sum, exclude it (the empty extension
contributes 0).
"""
import sys
from dataclasses import dataclass
from typing import Optional


sys.setrecursionlimit(10**6)


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = -float("inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left_gain  = max(gain(node.left),  0)
        right_gain = max(gain(node.right), 0)
        # Bent path through this node — compared to global, NOT returned.
        if node.val + left_gain + right_gain > best:
            best = node.val + left_gain + right_gain
        # Straight-down path returned to caller.
        return node.val + max(left_gain, right_gain)

    gain(root)
    return int(best)
