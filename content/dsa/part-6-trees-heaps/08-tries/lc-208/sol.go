// LC 208. Implement Trie (Prefix Tree)
package main

type Trie struct {
	children [26]*Trie
	isEnd    bool
}

func Constructor() Trie {
	return Trie{}
}

func (t *Trie) Insert(word string) {
	node := t
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if node.children[idx] == nil {
			node.children[idx] = &Trie{}
		}
		node = node.children[idx]
	}
	node.isEnd = true
}

func (t *Trie) Search(word string) bool {
	node := t.walk(word)
	return node != nil && node.isEnd
}

func (t *Trie) StartsWith(prefix string) bool {
	return t.walk(prefix) != nil
}

func (t *Trie) walk(s string) *Trie {
	node := t
	for i := 0; i < len(s); i++ {
		idx := s[i] - 'a'
		nxt := node.children[idx]
		if nxt == nil {
			return nil
		}
		node = nxt
	}
	return node
}
