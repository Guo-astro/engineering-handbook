# LC 102. Binary Tree Level Order Traversal
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """LC 102: return level-order traversal as a list of levels."""
    if root is None:
        return []
    result: List[List[int]] = []
    queue: deque = deque([root])
    while queue:
        level_size = len(queue)
        level: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result
