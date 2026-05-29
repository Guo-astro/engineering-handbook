# LC 98. Validate Binary Search Tree
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Bounded recursion. Each node must lie strictly in (lo, hi).
    Sedgewick & Wayne 4e §3.2 algo 3.3."""

    def check(node: Optional[TreeNode], lo: float, hi: float) -> bool:
        if node is None:
            return True
        if not (lo < node.val < hi):
            return False
        return check(node.left, lo, node.val) and check(node.right, node.val, hi)

    return check(root, float("-inf"), float("inf"))
