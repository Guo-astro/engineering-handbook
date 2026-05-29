# LC 1032. Stream of Characters

from collections import deque
from typing import List


class StreamChecker:
    """Aho-Corasick streaming matcher: query(c) returns True iff some pattern
    in the dictionary is a suffix of the characters streamed so far.

    The chapter teaches the offline matcher
        aho_corasick(patterns, text) -> {pattern: [start, ...]}
    LC 1032 is the same automaton with one character per call: the
    automaton state persists across calls, and query() returns True
    whenever the current state has any output.
    """

    def __init__(self, words: List[str]):
        # children[node][ch] -> child node id
        self.children: List[dict] = [{}]
        # failure link; root's fail is itself (0)
        self.fail: List[int] = [0]
        # whether any pattern's match ends at this node (after output inheritance)
        self.has_output: List[bool] = [False]

        # 1) Build the trie.
        for pat in words:
            node = 0
            for ch in pat:
                nxt = self.children[node].get(ch)
                if nxt is None:
                    nxt = len(self.children)
                    self.children.append({})
                    self.fail.append(0)
                    self.has_output.append(False)
                    self.children[node][ch] = nxt
                node = nxt
            self.has_output[node] = True

        # 2) Build failure links via BFS. BFS guarantees fail[parent] is
        #    computed before fail[child].
        queue = deque()
        for child in self.children[0].values():
            self.fail[child] = 0
            queue.append(child)
        while queue:
            u = queue.popleft()
            for ch, v in self.children[u].items():
                queue.append(v)
                f = self.fail[u]
                while f != 0 and ch not in self.children[f]:
                    f = self.fail[f]
                fv = self.children[f].get(ch, 0)
                if fv == v:
                    fv = 0
                self.fail[v] = fv
                # Output inheritance: any pattern ending on the failure
                # chain also ends here. Without this, the matcher misses
                # suffix-of-suffix matches (he inside she).
                if self.has_output[self.fail[v]]:
                    self.has_output[v] = True

        self.node = 0  # current automaton state, persisted across queries

    def query(self, letter: str) -> bool:
        # Advance one character: walk failure links until goto is defined,
        # then take the goto edge. Same shape as the offline scan.
        while self.node != 0 and letter not in self.children[self.node]:
            self.node = self.fail[self.node]
        self.node = self.children[self.node].get(letter, 0)
        return self.has_output[self.node]
