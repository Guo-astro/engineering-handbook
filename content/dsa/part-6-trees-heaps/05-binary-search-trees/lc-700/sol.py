# LC 700. Search in a Binary Search Tree
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


def search_bst(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """Walk down comparing keys; O(h) time, O(1) iterative space."""
    cur = root
    while cur is not None:
        if target == cur.val:
            return cur
        cur = cur.left if target < cur.val else cur.right
    return None
