# LC 297. Serialize and Deserialize Binary Tree
# Codec: preorder DFS + "#" sentinel for null children; round-trip is a same-shaped
# preorder DFS reading from an iterator over the tokens.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Codec:
    NULL = "#"
    SEP = ","

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Preorder DFS; emit value or NULL token for each slot."""
        out: list[str] = []

        def dfs(n: Optional[TreeNode]) -> None:
            if n is None:
                out.append(self.NULL)
                return
            out.append(str(n.val))               # visit (preorder)
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return self.SEP.join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Same preorder shape; consume one token per slot."""
        tokens = iter(data.split(self.SEP))

        def build() -> Optional[TreeNode]:
            tok = next(tokens)
            if tok == self.NULL:
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node

        return build()
