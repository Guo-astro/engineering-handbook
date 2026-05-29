# LC 208. Implement Trie (Prefix Tree)
from typing import List, Optional


class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: List[Optional["TrieNode"]] = [None] * 26
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            idx = ord(ch) - ord("a")
            nxt = node.children[idx]
            if nxt is None:
                return None
            node = nxt
        return node
