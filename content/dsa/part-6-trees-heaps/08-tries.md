---
title: "Tries"
description: "Children-map-plus-end-flag nodes give prefix walks in O(L) on query length. The autocomplete and IP-routing problem family where prefix structure is the whole point."
slug: 08-tries
part: 6
chapter: 8
difficulty: intermediate
prerequisites:
  - part-6-trees-heaps/00-binary-tree-fundamentals
  - part-1-linear-data-structures/03-hash-maps
date_updated: 2026-05-25
languages: [python, java, cpp, go]
canonical_test: LC-208
widgets: [w-20-trie]
ladder:
  core: [LC-208, LC-720, LC-212]
  stretch: [LC-211, LC-1268]
  star: LC-208
---

# Tries

Every keystroke on the iPhone keyboard walks a trie. So does every URL the browser autocompletes, every IP route the Linux kernel forwards, every word the spell-checker validates inside the editor you're typing into right now. The data structure dates to a 1959 paper by René de la Briandais and a 1960 paper by Edward Fredkin (Fredkin coined the name from "re*trie*val"), and it is still the answer to the same question now that it was then: given a set of strings, answer prefix queries in time proportional to the query, not to the size of the set.

A hash set can answer "is `cat` a word?" in O(L) on the length of `cat`. What it cannot do, without rescanning every key, is answer *"list every word that starts with `ca`"*. That is the gap a trie fills.[^1] The cost of filling it is structural: a tree whose edges are characters, whose paths spell prefixes, whose terminal flags say "the path you walked here is a complete word." Insert and search both walk one node per character; the dictionary's redundancy collapses into shared chains. *Algorithms* 4e §5.2 calls the structure an R-way trie; the LeetCode problem set calls it a prefix tree; both mean the same six lines of code and the same three operations.[^2]

The two payoff problems are LC 211 (wildcard search) and LC 212 (word-search on a 2D grid). LC 212 is the harder one. Per-word DFS without a trie times out on LC's hardest case; trie-accelerated DFS prunes whole subtrees of patterns in a single null-child check, and the same problem becomes comfortable.

## What's in the structure

A trie is a tree of characters. Each node holds an array (or hash map) of children indexed by character, plus a single boolean called `is_end` that says "an inserted word terminates exactly here." The root holds no character; its children represent the alphabet's first letters; descending one edge consumes one character of the input. A path from root to any node *is* the prefix it represents.

The insert operation walks the path the new word's characters dictate, allocating nodes wherever the path doesn't exist yet, and flips `is_end` on at the final node. Search does the same walk and asks two questions at the end: did we reach a non-null node, and is `is_end` set there? Search returns true only when both are. `startsWith` does the same walk and asks only the first question.

```python
class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            i = ord(ch) - ord("a")
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_end = True

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            i = ord(ch) - ord("a")
            nxt = node.children[i]
            if nxt is None:
                return None
            node = nxt
        return node
```

**Solution** — Python ([Java](./08-tries/lc-208/sol.java) · [C++](./08-tries/lc-208/sol.cpp) · [Go](./08-tries/lc-208/sol.go))

```python
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
```

Three things to read off the code. The walk is shared between `search` and `startsWith`; `_walk` does the work for both. The only functional difference between the two is the trailing `node.is_end` check; everything else is identical. And every operation is exactly `len(input)` iterations long, with one array index and one null check per character. There is no recursion, no balancing, no rotation. The shape of the data does the work.

The widget animates inserting `car`, `cat`, `card` into an empty trie, then walking the prefix `ca`. The shared `ca` chain is the chapter's central image:

> **Interactive widget:** [Trie — insert + prefix walk + frequency autocomplete](../widgets/w-20-trie.yml) (panel `default`) — rendered on the website; the YAML spec describes the keyframes.

*Static fallback: the trie starts as a lone root. Inserting car creates the chain root → c → a → r and flags r as is_end. Inserting cat reuses the c and a nodes already on the path, then creates a t-branch off n_ca; only one new node was allocated. Inserting card reuses c, a, and r; r already had is_end set (from car), and now also gains a d-child that is_end (for card). The walk on ca follows two edges and reports startsWith = true; cost is independent of how many words are in the trie.*

The single observation that makes this O(L) per operation is that the path length equals the input length. Branching factor `R` enters as a constant in the per-edge index step (array: O(1); hash map: O(1) average) but does not affect path length.[^1] A hash table's lookup is also Ω(L), since the hash function reads every character of the key, so the trie's O(L) is *not* asymptotically slower than a hash on point lookup; it is *additionally* able to answer prefix queries the hash cannot.[^3]

## What `is_end` is and is not

The biggest bug authors write into a fresh trie implementation is collapsing two concepts that are not the same.

`is_end` is a flag that says "an inserted word terminates here." Whether the node has children is a separate fact about the node's position in the structure. After inserting `car` and `card`, the node `n_car` is `is_end = true` AND has a `d`-child for `n_card`. Treating `is_end` as a synonym for "leaf" silently breaks `search("car")` once `card` joins the dictionary, or it breaks `startsWith("car")` because the implementation kept testing `is_end` instead of testing for a non-null node.

> [!IMPORTANT]
> `search` checks `is_end`. `startsWith` does not. Paste `search` into `startsWith` and forget to drop the `is_end` test, and `startsWith("a")` returns false after `insert("apple")`, a wrong answer that LC 208's grader catches but a non-grading reader would not. The LC 208 official editorial calls this out by name as the reason `searchPrefix` is the shared helper and `search` adds the `is_end` check on top.[^4]

There's a second invariant worth stating once. Inserting `apple` produces the chain `a → p → p → l → e`, with the *first* `p` being a separate node from the *second* `p`. Duplicate characters in a word are not collapsed; the trie's branching is per-position, not per-letter. Read the code as: each character of the input chooses *the next bucket among the current node's R children*, regardless of which character was chosen at the previous step. Internalize that and tries become routine.

## Choosing the children container

The R-way array shown above is the textbook default and the right pick for a fixed lowercase-English alphabet. Other constraints argue for other shapes.

A 26-pointer array per node is fast: one indexed dereference per descent, full cache locality on a contiguous 26-slot row, at a memory cost of `R` pointers per node whether the node has 1 child or 26. On a trie with 100,000 nodes and 8-byte pointers, that's 20 MB just for the children arrays, most of it null. Sedgewick & Wayne's R-way trie analysis frames this trade-off explicitly: pure array nodes give the fastest descent at the cost of `R` pointers per node; map-based nodes drop memory to `O(d_v)` per node, where `d_v` is the number of distinct child characters actually used, and pay one hash per edge instead of one indexed read.[^3]

| Container | Edge cost | Memory per node | Use when |
|---|---|---|---|
| `children[R]` (R-way array) | O(1) indexed read | R pointers, dense | Small fixed alphabet (lowercase, DNA, IPv4 nibbles); LC 208 default |
| Hash-map children | O(1) hash, average | `O(d_v)` actual children | Unicode, arbitrary bytes, large/unknown alphabet |
| Ternary search trie | O(log R) descent | 3 pointers per node | Need ordered iteration without R-array waste; Sedgewick's `algs4` ships TrieST.java[^3] |

Production implementations bend further. The Linux kernel's IP routing table uses a *compressed* trie (radix tree) that merges any chain of single-child nodes into one edge labeled with a multi-character string; memory drops from `O(R)` per character to `O(R)` per branch point, while the search cost stays bounded by total characters compared.[^2] Donald Morrison's 1968 PATRICIA paper introduced the compressed trie idea for exactly this reason: long, sparsely-branching keys waste enormous memory in the uncompressed form. For the chapter's CORE problems (LC 208, LC 720, LC 212) the R-way array is correct and easy to reason about; the compressed variant earns its keep when keys are long and prefix sharing is sparse, and the variants table below carries the cross-reference.

## When the walk is not a single path

LC 208 is the mechanics. The two payoff problems are LC 211 and LC 212. Both keep the trie's structure intact and replace the linear walk with a recursive search.

### LC 211: wildcards and a tree-shaped walk

Given a stream of `addWord` and `search` calls, where a search query may contain `.` characters that match any single letter, return whether the dictionary contains *any* word matching the query.

The signal: a single-character wildcard turns the walk from "follow exactly one edge" into "try every non-null child." The walk is no longer a path; it's a depth-first search over the trie subtree rooted at the current node.

```python
def search(self, word):
    return self._dfs(self.root, word, 0)

def _dfs(self, node, word, i):
    if i == len(word):
        return node.is_end
    ch = word[i]
    if ch == ".":
        for child in node.children:
            if child is not None and self._dfs(child, word, i + 1):
                return True
        return False
    nxt = node.children[ord(ch) - ord("a")]
    if nxt is None:
        return False
    return self._dfs(nxt, word, i + 1)
```

**Solution** — Python ([Java](./08-tries/lc-211/sol.java) · [C++](./08-tries/lc-211/sol.cpp) · [Go](./08-tries/lc-211/sol.go))

```python
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
```

The two branches are the entire algorithm. Concrete character: descend to that one child or fail. Wildcard: try every existing child; succeed if any subtree contains a match.

LC 211's worst case is `O(R^k)` where `k` is the number of dots: a query of all dots against an `R`-branching trie expands the entire subtree. The problem statement caps queries at 2 dots, which bounds the worst case at `26^2 = 676` paths per search.[^5] That cap is structural, not optional. Drop it and the algorithm needs an Aho-Corasick-style automaton with suffix links, which is a different chapter and a much harder one.[^6]

### LC 212: the trie as a prune oracle

Given a 2D grid of letters and a list of words, return every word that can be spelled by walking adjacent cells (no cell reused within a word). The naive solution is one DFS per word: for each word in the dictionary, try every starting cell and walk the grid. With a dictionary of 30,000 words, words up to 10 characters long, and a 12×12 board, that approach times out everywhere. LC 212 was specifically designed to fail it.

The trie-accelerated version inverts the loop. Insert all the words into a trie. Then run *one* DFS over the board, advancing both the cell pointer and the trie node pointer in lockstep. At every step, the next character on the board must equal the edge to descend; a missing trie child is an instant backtrack signal that prunes *every* word sharing the impossible prefix at once.

```python
def findWords(self, board, words):
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.word = w  # store the word at its terminal node

    rows, cols = len(board), len(board[0])
    found = []

    def dfs(r, c, parent):
        ch = board[r][c]
        node = parent.children.get(ch)
        if node is None:
            return                       # the prune
        if node.word:
            found.append(node.word)
            node.word = ""               # suppress re-finding
        board[r][c] = "#"
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, node)
        board[r][c] = ch
        if not node.children:
            parent.children.pop(ch, None) # shrink the trie on the fly

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return found
```

**Solution** — Python ([Java](./08-tries/lc-212/sol.java) · [C++](./08-tries/lc-212/sol.cpp) · [Go](./08-tries/lc-212/sol.go))

```python
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
```

Three details earn their lines. Storing the word string at the terminal node (not just `is_end`) lets the DFS report finds without reconstructing the path it took. Setting `node.word = ""` after a find suppresses the duplicate finds that would otherwise pile up as the DFS keeps reaching the same terminal from different paths. Pruning leaf nodes upward (`parent.children.pop(ch, None)` when the current node has no children left) shrinks the trie as words are exhausted, so later DFS sweeps run against a smaller structure.[^7]

The asymmetry between LC 211 and LC 212 is worth naming. In LC 211 the trie is the answer-bearing structure; the search returns based on what's in it. In LC 212 the trie is a *lookahead pruner* for a search whose state lives in the grid. The two roles are different, and "the trie can be a pruner" is one of the highest-leverage patterns in problem-pattern-matching across all of competitive programming. Aho-Corasick generalizes the LC 212 idea to multi-pattern text search by adding suffix links to the trie.[^6]

## What it actually costs

| Operation | Time | Space (per node) | Notes |
|---|---|---|---|
| `insert(word)` | O(L) | O(R) array; O(d_v) hash-map | Each character: one index + one null check + at most one allocation.[^1][^3] |
| `search(word)` | O(L) | unchanged | Same walk plus an `is_end` check at the end.[^1] |
| `startsWith(prefix)` | O(L) | unchanged | Walk only; no `is_end` check.[^1] |
| Build (n words, total chars m) | O(m) | O(mR) worst case array; O(m) hash-map | All inserts together. |
| LC 211 search with k dots | O(R^k) worst | unchanged | Bounded at `26^2 = 676` by LC's "at most 2 dots" cap.[^5] |
| LC 212 trie-accelerated DFS | O(M·N · 4 · 3^(L−1)) worst | O(K) trie size | M·N grid cells, L = max word length, K = total word characters; the prune cuts the constant factor by a wide margin in practice.[^7] |

Notation: `L` = length of the operation's input string; `R` = alphabet size (26 lowercase, 256 ASCII, larger for Unicode); `m` = sum of all key lengths in the trie; `d_v` = distinct child characters at node v.

The walk-length bound is structural: trie depth equals the longest key, and each operation touches one node per character of its input. The branching factor enters the per-edge cost (O(1) array, O(1) average hash) but not the path length.[^1] Tries are *memory-expensive* in the R-way array form, and there is no point pretending otherwise; if your dictionary's keys are long and sparsely branching, the radix tree is the production answer.[^2]

### Pattern variants worth knowing

| Variant | When to reach for it | Notes |
|---|---|---|
| **R-way array** (the default in this chapter) | Small fixed alphabet (lowercase, DNA, hex) | One indexed read per edge; full cache locality |
| **Hash-map children** | Unicode, arbitrary bytes, unknown alphabet | One hash per edge; memory drops from R to actual `d_v` |
| **Compressed trie / radix tree** (Patricia) | Long keys, sparse branching, memory-bound systems (IP routing tables, file-path indexes) | Single-child chains merge into multi-character edge labels; Morrison 1968.[^2] |
| **Ternary search trie** | Want ordered iteration with O(log R) descent and modest memory | Sedgewick's `algs4` ships TrieST.java; node has lt/eq/gt children.[^3] |
| **DAWG** (directed acyclic word graph) | Static dictionary; want to share *suffixes* in addition to prefixes | Same node may be reached by multiple paths; saves more memory than a trie at the cost of being un-mutable |
| **Suffix tree** | Substring queries, not prefix queries (a different problem) | A trie of all suffixes of one string; built in O(n) by Ukkonen's algorithm |
| **Aho-Corasick** | Multi-pattern substring search in a text | Trie + failure links; the LC 212 idea, generalized.[^6] |

The compressed trie matters often enough that it deserves the explicit cross-reference, but its constants comparison against the R-way array is implementation-specific and outside this chapter's scope; treat it as the production fallback when memory bites. DAWG and suffix tree are entirely different problems that happen to share the trie's tree-of-characters skeleton.

## Where readers go wrong

> [!WARNING]
> **Confusing `is_end` with leafness.** Writing `if node.is_end: it has no children`, or believing only leaves can be `is_end`. After inserting `car` and `card`, `n_car` is `is_end = true` AND has a `d`-child. Treat `is_end` and "has children" as orthogonal flags. `search` checks the first; `startsWith` checks neither.[^4]

> [!WARNING]
> **Forgetting that `startsWith` ignores `is_end`.** Pasting `search` into `startsWith` and leaving the `is_end` check returns false on `startsWith("a")` after `insert("apple")` is the only insert. The walk reaches a non-null node, which is exactly when `startsWith` should return true.[^4]

> [!WARNING]
> **Sizing the children array against the wrong alphabet.** A `[26]` array under input that includes uppercase or digits computes `idx = ord('A') - ord('a') = -32` and indexes into garbage. A `[128]` array under purely lowercase input wastes ~5x the memory it needs. Read the constraints; use `[26]` for LC 208/211/212/720, switch to a hash map when alphabet is Unicode or unknown.[^3]

> [!WARNING]
> **Per-word DFS on LC 212.** Looping over words and running grid DFS for each one is `O(words × cells × 4^L)` and times out at LC's hard test case. The trie-accelerated version is one DFS over the board with the dictionary collapsed into a prune oracle. The two approaches are not equivalent under LC's time budget.[^7]

> [!WARNING]
> **Skipping the `is_end = false` step after a find in LC 212.** Once the DFS reaches a terminal and records the word, leaving `is_end = true` (or leaving `node.word` non-empty in the variant shown above) causes the same word to be re-found from every new starting cell that can reach it. The answer set deduplicates; the work does not. Clear the marker the first time you find the word.[^7]

## Problem ladder

### CORE (solve all three to claim chapter mastery)

- [LC 208 — Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) [Medium] • trie-fundamentals-insert-search-startswith ★
- [LC 720 — Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) [Easy] • trie-bfs-or-sort-prefix-incremental
- [LC 212 — Word Search II](https://leetcode.com/problems/word-search-ii/) [Hard] • trie-accelerated-backtracking-on-grid

### STRETCH (optional)

- [LC 211 — Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) [Medium] • trie-with-wildcard-dfs
- [LC 1268 — Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) [Medium] • trie-prefix-with-sorted-collection

LC 211 lives in STRETCH despite carrying its own worked-example treatment in the prose because the wildcard mechanic is a *natural follow-on* to LC 208 rather than an independent skill. Most readers who get LC 208 right get LC 211 right on the next sitting.

## Where this leads

[Word Search II via backtracking](../part-7-recursion-backtracking/05-word-search.md) owns LC 79 (the single-word version) and treats the recursion shape on its own; the trie pruning that makes the dictionary version (LC 212) tractable lives here. [KMP and string pattern matching](../part-12-strings-pattern-matching/02-kmp.md) is the natural next step for anyone whose interest is multi-pattern text search. Aho-Corasick is a trie with failure links bolted on, and the R-way trie you can now build is its substrate.

## References

[^1]: Wikipedia contributors, "Trie," last edited March 2026, [en.wikipedia.org/wiki/Trie](https://en.wikipedia.org/wiki/Trie).

[^2]: Wikipedia's "Radix tree" article documents the compressed-trie variant and credits Donald R. Morrison, "PATRICIA — Practical Algorithm to Retrieve Information Coded in Alphanumeric," *Journal of the ACM* 15(4), October 1968, pp. 514-534, doi:[10.1145/321479.321481](https://doi.org/10.1145/321479.321481).

[^3]: Robert Sedgewick and Kevin Wayne, *Algorithms*, 4th ed., Addison-Wesley, 2011, §5.2 Tries. Online supplement at [algs4.cs.princeton.edu/52trie](https://algs4.cs.princeton.edu/52trie/).

[^4]: LeetCode official problem and editorial for LC 208, "Implement Trie (Prefix Tree)," difficulty Medium. Cross-confirmed via NeetCode's [implement-prefix-tree problem page](https://neetcode.io/problems/implement-prefix-tree/question).

[^5]: LeetCode 211, "Design Add and Search Words Data Structure," constraints page at [leetcode.com/problems/design-add-and-search-words-data-structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

[^6]: cp-algorithms, "Aho-Corasick algorithm," last updated April 2025, [cp-algorithms.com/string/aho_corasick.html](https://cp-algorithms.com/string/aho_corasick.html).

[^7]: AlgoMonster editorial for LC 212, "Word Search II," at [algo.monster/liteproblems/212](https://algo.monster/liteproblems/212)
