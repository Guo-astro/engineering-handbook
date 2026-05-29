# LC 110. Balanced Binary Tree
"""LC 110 Balanced Binary Tree, height-or-sentinel post-order recursion."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Return True iff every node's left/right subtree heights differ by <= 1."""

    def height(node: Optional[TreeNode]) -> int:
        # Returns subtree height, or -1 if any descendant is unbalanced.
        if node is None:
            return 0
        lh = height(node.left)
        if lh == -1:
            return -1
        rh = height(node.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return height(root) != -1
