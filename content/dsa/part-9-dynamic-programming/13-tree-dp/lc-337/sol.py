# LC 337. House Robber III
# mirrors the two-state tuple-return
# pattern (pair-return state machine on tree).
"""LC 337. Maximum money you can rob without alerting the police.

Two adjacent nodes cannot both be robbed. The recurrence at each node is
a small state machine: returning a 2-tuple (rob_this, skip_this), where
rob_this = node.val + skip_left + skip_right (children must be skipped)
skip_this = max(rob_left, skip_left) + max(rob_right, skip_right) (free choice).
The wrapper takes max(rob_root, skip_root). One post-order pass; O(n) time.
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


def rob(root: Optional[TreeNode]) -> int:
    def helper(node: Optional[TreeNode]) -> Tuple[int, int]:
        if node is None:
            return (0, 0)  # (rob_this, skip_this) for an empty subtree
        rob_l, skip_l = helper(node.left)
        rob_r, skip_r = helper(node.right)
        # Robbing this node forces both children to be skipped.
        rob_this = node.val + skip_l + skip_r
        # Skipping this node leaves each child's choice free.
        skip_this = max(rob_l, skip_l) + max(rob_r, skip_r)
        return (rob_this, skip_this)

    return max(helper(root))
