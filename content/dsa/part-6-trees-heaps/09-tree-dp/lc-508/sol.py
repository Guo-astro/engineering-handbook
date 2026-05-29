# LC 508. Most Frequent Subtree Sum
"""LC 508. Return every subtree sum that ties for the highest frequency.

Shape 2 of tree DP: post-order returns aggregate, side accumulator records
every value the helper produces. The helper's return is what the parent
needs (the subtree sum); the answer lives in a separate channel (a Counter
keyed on every sum the recursion has ever produced).
"""
import sys
from collections import Counter
from dataclasses import dataclass
from typing import List, Optional


sys.setrecursionlimit(10**6)


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def find_frequent_tree_sum(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    counts: Counter[int] = Counter()

    def subtree_sum(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
        counts[s] += 1
        return s

    subtree_sum(root)
    best = max(counts.values())
    return [s for s, c in counts.items() if c == best]
