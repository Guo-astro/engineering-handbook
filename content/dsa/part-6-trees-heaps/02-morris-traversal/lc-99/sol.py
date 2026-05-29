# LC 99. Recover Binary Search Tree

from typing import Optional


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """Recover a BST in which exactly two nodes are swapped, in O(1) space.

        Reference: J. M. Morris, 'Traversing binary trees simply and cheaply',
        Information Processing Letters 9(5):197-200, 1979.

        Layers the LC 99 'two witnesses' pattern on top of Morris inorder:
        track prev across the visit step; capture first on the first
        violation; keep updating second on every violation; swap at the end.
        """
        first: Optional[TreeNode] = None
        second: Optional[TreeNode] = None
        prev: Optional[TreeNode] = None

        curr = root
        while curr is not None:
            if curr.left is None:
                # Visit step.
                if prev is not None and curr.val < prev.val:
                    if first is None:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find inorder predecessor: rightmost in curr's left subtree.
                pred = curr.left
                while pred.right is not None and pred.right is not curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = curr            # install thread, descend left
                    curr = curr.left
                else:
                    pred.right = None            # tear down thread before visit
                    if prev is not None and curr.val < prev.val:
                        if first is None:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        if first is not None and second is not None:
            first.val, second.val = second.val, first.val
