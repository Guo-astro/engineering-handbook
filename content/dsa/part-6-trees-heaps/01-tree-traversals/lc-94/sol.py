# LC 94. Binary Tree Inorder Traversal
#   [1,null,2,3] -> [1,3,2], [] -> [], [1] -> [1], [1,2,3,4,5,null,6] -> [4,2,5,1,3,6]
#.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """Recursive inorder. The five-line skeleton; visit on the middle line."""
    out: List[int] = []

    def dfs(n: Optional[TreeNode]) -> None:
        if n is None:
            return
        dfs(n.left)
        out.append(n.val)         # visit
        dfs(n.right)

    dfs(root)
    return out


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative inorder via explicit stack. Push left chain, pop, pivot right.
    Invariant: after every iteration, `cur` points to the next subtree to descend
    into; `stack` holds every node whose left subtree has been descended into
    but whose value has not yet been emitted.
    """
    out: List[int] = []
    stack, cur = [], root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right            # pivot to right subtree
    return out


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative preorder. Push right BEFORE left so left pops next."""
    out: List[int] = []
    if root is None:
        return out
    stack = [root]
    while stack:
        n = stack.pop()
        out.append(n.val)
        if n.right is not None:
            stack.append(n.right)
        if n.left is not None:
            stack.append(n.left)
    return out


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative postorder via the two-stack / reverse trick: build root,right,left
    then reverse to left,right,root.
    """
    out: List[int] = []
    if root is None:
        return out
    stack = [root]
    while stack:
        n = stack.pop()
        out.append(n.val)
        if n.left is not None:
            stack.append(n.left)
        if n.right is not None:
            stack.append(n.right)
    out.reverse()
    return out
