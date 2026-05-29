# LC 211. Design Add and Search Words Data Structure
# [addWord("bad"), addWord("dad"), addWord("mad"), search("pad")=False,
#  search("bad")=True, search(".ad")=True, search("b..")=True] passes.
# Wildcard '.' matches any one lowercase letter; recurse over all
# non-null children at a wildcard step. The LC 211 problem caps queries
# at 2 dots, bounding worst case at 26^2 = 676 paths per search
#.
from typing import List, Optional


class _Node:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: List[Optional["_Node"]] = [None] * 26
        self.is_end: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = _Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = _Node()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node: _Node, word: str, i: int) -> bool:
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == ".":
            for child in node.children:
                if child is not None and self._dfs(child, word, i + 1):
                    return True
            return False
        idx = ord(ch) - ord("a")
        nxt = node.children[idx]
        if nxt is None:
            return False
        return self._dfs(nxt, word, i + 1)
