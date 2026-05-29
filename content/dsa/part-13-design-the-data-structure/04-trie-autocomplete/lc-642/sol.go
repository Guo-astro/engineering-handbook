// LC 642. Design Search Autocomplete System (Premium)
// []pair sorted DESC score, ASC word, capped at kCap.
package main

const kCap = 10

type pair struct {
	score int
	word  string
}

type node struct {
	children map[byte]*node
	isEnd    bool
	top      []pair // DESC score, ASC word, capped at kCap
}

type AutocompleteTrie struct {
	root   *node
	scores map[string]int
}

func NewAutocompleteTrie() *AutocompleteTrie {
	return &AutocompleteTrie{root: newNode(), scores: map[string]int{}}
}

func newNode() *node {
	return &node{children: map[byte]*node{}}
}

func (a *AutocompleteTrie) Input(word string, freq int) {
	a.scores[word] = freq
	n := a.root
	insertTop(&n.top, freq, word)
	for i := 0; i < len(word); i++ {
		ch := word[i]
		nxt, ok := n.children[ch]
		if !ok {
			nxt = newNode()
			n.children[ch] = nxt
		}
		n = nxt
		insertTop(&n.top, freq, word)
	}
	n.isEnd = true
}

func (a *AutocompleteTrie) TopK(prefix string, k int) []string {
	if k <= 0 {
		return []string{}
	}
	n := a.root
	for i := 0; i < len(prefix); i++ {
		nxt, ok := n.children[prefix[i]]
		if !ok {
			return []string{}
		}
		n = nxt
	}
	limit := k
	if limit > len(n.top) {
		limit = len(n.top)
	}
	out := make([]string, 0, limit)
	for i := 0; i < limit; i++ {
		out = append(out, n.top[i].word)
	}
	return out
}

func insertTop(top *[]pair, score int, word string) {
	for i, p := range *top {
		if p.word == word {
			*top = append((*top)[:i], (*top)[i+1:]...)
			break
		}
	}
	pos := len(*top)
	for i, p := range *top {
		if score > p.score || (score == p.score && word < p.word) {
			pos = i
			break
		}
	}
	*top = append(*top, pair{})
	copy((*top)[pos+1:], (*top)[pos:])
	(*top)[pos] = pair{score: score, word: word}
	if len(*top) > kCap {
		*top = (*top)[:kCap]
	}
}
