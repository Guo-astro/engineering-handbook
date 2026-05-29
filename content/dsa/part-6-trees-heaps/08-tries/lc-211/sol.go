// LC 211. Design Add and Search Words Data Structure
// LC 211 canonical sequence passes.
// '.' matches any one lowercase letter; recurse across all non-nil
// children at a wildcard step.
package main

type WordDictionary struct {
	root *wdNode
}

type wdNode struct {
	children [26]*wdNode
	isEnd    bool
}

func ConstructorWD() WordDictionary {
	return WordDictionary{root: &wdNode{}}
}

func (d *WordDictionary) AddWord(word string) {
	node := d.root
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if node.children[idx] == nil {
			node.children[idx] = &wdNode{}
		}
		node = node.children[idx]
	}
	node.isEnd = true
}

func (d *WordDictionary) Search(word string) bool {
	return dfsWD(d.root, word, 0)
}

func dfsWD(node *wdNode, word string, i int) bool {
	if i == len(word) {
		return node.isEnd
	}
	ch := word[i]
	if ch == '.' {
		for _, child := range node.children {
			if child != nil && dfsWD(child, word, i+1) {
				return true
			}
		}
		return false
	}
	nxt := node.children[ch-'a']
	if nxt == nil {
		return false
	}
	return dfsWD(nxt, word, i+1)
}
