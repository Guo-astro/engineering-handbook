# LC: none — chapter mechanic (AVL insert with rebalance)
from typing import Optional


class Node:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.height = 1  # leaf: 1; height(None) := 0


def height(node: Optional[Node]) -> int:
    return node.height if node is not None else 0


def balance_factor(node: Node) -> int:
    # BF > 0 => left-heavy; BF < 0 => right-heavy.
    return height(node.left) - height(node.right)


def _update_height(node: Node) -> None:
    node.height = 1 + max(height(node.left), height(node.right))


def _rotate_right(y: Node) -> Node:           # fixes LL
    x = y.left
    assert x is not None
    t2 = x.right
    x.right = y
    y.left = t2
    _update_height(y)
    _update_height(x)
    return x


def _rotate_left(x: Node) -> Node:            # fixes RR (mirror of right)
    y = x.right
    assert y is not None
    t2 = y.left
    y.left = x
    x.right = t2
    _update_height(x)
    _update_height(y)
    return y


def insert(root: Optional[Node], key: int) -> Node:
    """Insert key into AVL rooted at root; return new root."""
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # duplicates ignored

    _update_height(root)
    bf = balance_factor(root)

    if bf > 1 and root.left is not None and key < root.left.key:        # LL
        return _rotate_right(root)
    if bf < -1 and root.right is not None and key > root.right.key:     # RR
        return _rotate_left(root)
    if bf > 1 and root.left is not None and key > root.left.key:        # LR
        root.left = _rotate_left(root.left)
        return _rotate_right(root)
    if bf < -1 and root.right is not None and key < root.right.key:     # RL
        root.right = _rotate_right(root.right)
        return _rotate_left(root)
    return root
