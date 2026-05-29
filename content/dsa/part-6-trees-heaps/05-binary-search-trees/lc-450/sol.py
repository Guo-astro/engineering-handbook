# LC 450. Delete Node in a BST
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


def _min_node(node: TreeNode) -> TreeNode:
    while node.left is not None:
        node = node.left
    return node


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Three-case delete (Hibbard 1962). CLRS §12.3 Theorem 12.4."""
    if root is None:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Found x with x.val == key.
        if root.left is None and root.right is None:
            return None              # case 1: leaf
        if root.left is None:
            return root.right        # case 2a: only right child
        if root.right is None:
            return root.left         # case 2b: only left child
        succ = _min_node(root.right) # case 3: two children
        root.val = succ.val
        root.right = delete_node(root.right, succ.val)
    return root
