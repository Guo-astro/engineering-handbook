// LC 1032. Stream of Characters

package streamchecker

type StreamChecker struct {
	children  []map[byte]int
	fail      []int
	hasOutput []bool
	node      int // current automaton state
}

func Constructor(words []string) StreamChecker {
	sc := StreamChecker{
		children:  []map[byte]int{{}},
		fail:      []int{0},
		hasOutput: []bool{false},
	}

	// 1) Build the trie.
	for _, pat := range words {
		cur := 0
		for i := 0; i < len(pat); i++ {
			ch := pat[i]
			nxt, ok := sc.children[cur][ch]
			if !ok {
				nxt = len(sc.children)
				sc.children = append(sc.children, map[byte]int{})
				sc.fail = append(sc.fail, 0)
				sc.hasOutput = append(sc.hasOutput, false)
				sc.children[cur][ch] = nxt
			}
			cur = nxt
		}
		sc.hasOutput[cur] = true
	}

	// 2) Build failure links via BFS.
	queue := make([]int, 0)
	for _, child := range sc.children[0] {
		sc.fail[child] = 0
		queue = append(queue, child)
	}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for ch, v := range sc.children[u] {
			queue = append(queue, v)
			f := sc.fail[u]
			for f != 0 {
				if _, ok := sc.children[f][ch]; ok {
					break
				}
				f = sc.fail[f]
			}
			fv, ok := sc.children[f][ch]
			if !ok {
				fv = 0
			}
			if fv == v {
				fv = 0
			}
			sc.fail[v] = fv
			// Output inheritance.
			if sc.hasOutput[sc.fail[v]] {
				sc.hasOutput[v] = true
			}
		}
	}

	return sc
}

func (sc *StreamChecker) Query(letter byte) bool {
	for sc.node != 0 {
		if _, ok := sc.children[sc.node][letter]; ok {
			break
		}
		sc.node = sc.fail[sc.node]
	}
	nxt, ok := sc.children[sc.node][letter]
	if !ok {
		sc.node = 0
	} else {
		sc.node = nxt
	}
	return sc.hasOutput[sc.node]
}
