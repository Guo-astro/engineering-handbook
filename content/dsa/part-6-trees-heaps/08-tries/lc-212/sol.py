# LC 212. Word Search II
# board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
#        ["i","f","l","v"]], words=["oath","pea","eat","rain"]
# returns ["oath", "eat"].
#
# Trie-accelerated backtracking: insert all words into a trie keyed by
# board characters; DFS from each cell advances both the cell pointer
# AND the trie node pointer. A missing trie child is an instant
# backtrack — the entire subtree of patterns sharing that prefix is
# pruned in O(1). After finding a word, set is_end = False to suppress
# re-finding; prune leaf nodes upward to shrink the trie on the fly.
from typing import Dict, List


class _Node:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: Dict[str, "_Node"] = {}
        self.word: str = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = _Node()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, _Node())
            node.word = w

        rows, cols = len(board), len(board[0])
        found: List[str] = []

        def dfs(r: int, c: int, parent: _Node) -> None:
            ch = board[r][c]
            node = parent.children.get(ch)
            if node is None:
                return
            if node.word:
                found.append(node.word)
                node.word = ""  # suppress re-finding
            board[r][c] = "#"  # mark visited
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = ch  # restore
            # Prune dead branches.
            if not node.children:
                parent.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return found
