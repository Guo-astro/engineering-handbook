# LC 642. Design Search Autocomplete System (Premium)
# Frequency-extended trie. Each node caches the top-K (score DESC, word ASC)
# words that pass through it; `input(word, freq)` refreshes the cache on
# every node along the insert path; `topk(prefix, k)` walks to the prefix
# node and reads the cache directly. O(L * K) per insert; O(L + k) per
# query. The same code answers the LC 1268 free contract by reading the
# top-3 lex-smallest words (set freq = -ord-string for lex order).
from typing import Dict, List, Tuple


class TrieNode:
    __slots__ = ("children", "is_end", "top")

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end: bool = False
        # Sorted DESC by score, ties ASC by word; capped at K_CAP.
        self.top: List[Tuple[int, str]] = []


K_CAP = 10  # per-node cap; supports any k <= K_CAP at lookup time


def _insert_top(top: List[Tuple[int, str]], score: int, word: str) -> None:
    for i, (_s, w) in enumerate(top):
        if w == word:
            top.pop(i)
            break
    placed = False
    for i, (s, w) in enumerate(top):
        if score > s or (score == s and word < w):
            top.insert(i, (score, word))
            placed = True
            break
    if not placed:
        top.append((score, word))
    if len(top) > K_CAP:
        top.pop()


class AutocompleteTrie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.scores: Dict[str, int] = {}

    def input(self, word: str, freq: int) -> None:
        """Insert or refresh `word` with score `freq`. New freq REPLACES prior."""
        self.scores[word] = freq
        node = self.root
        _insert_top(node.top, freq, word)
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            _insert_top(node.top, freq, word)
        node.is_end = True

    def topk(self, prefix: str, k: int) -> List[str]:
        if k <= 0:
            return []
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return [w for (_s, w) in node.top[:k]]
