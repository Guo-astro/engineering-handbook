# LC 968. Binary Tree Cameras
# mirrors the three-state DP
# pattern (state-machine reduction on tree).
"""LC 968. Minimum cameras to monitor every node.

Each node returns one of three states to its parent:
  0 = NEEDS_COVER   (this node is not yet monitored; parent must cover it)
  1 = HAS_CAMERA    (this node holds a camera; covers itself and parent)
  2 = COVERED       (this node is monitored by a child; parent has no duty)
The rule:
  - If any child needs cover: place a camera here (state 1, count++).
  - If any child has a camera: this node is COVERED (state 2).
  - Otherwise (both children covered): this node NEEDS_COVER (state 0).
A null leaf returns COVERED (state 2): the empty subtree imposes no obligation.
The wrapper checks the root: if it returns NEEDS_COVER, place one final camera.
"""
import sys
from dataclasses import dataclass
from typing import Optional


sys.setrecursionlimit(10**6)

NEEDS_COVER = 0
HAS_CAMERA = 1
COVERED = 2


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def min_camera_cover(root: Optional[TreeNode]) -> int:
    cameras = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal cameras
        if node is None:
            return COVERED
        l = dfs(node.left)
        r = dfs(node.right)
        # Any child unmonitored — place a camera here.
        if l == NEEDS_COVER or r == NEEDS_COVER:
            cameras += 1
            return HAS_CAMERA
        # Any child holds a camera — this node is covered by it.
        if l == HAS_CAMERA or r == HAS_CAMERA:
            return COVERED
        # Both children covered, none has a camera — this node needs cover.
        return NEEDS_COVER

    if dfs(root) == NEEDS_COVER:
        cameras += 1
    return cameras
