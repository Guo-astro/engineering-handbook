// LC 684. Redundant Connection
package main

type DSU struct {
	parent []int
	rank   []int
}

func NewDSU(n int) *DSU {
	d := &DSU{parent: make([]int, n+1), rank: make([]int, n+1)}
	for i := 0; i <= n; i++ {
		d.parent[i] = i
	}
	return d
}

func (d *DSU) Find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.Find(d.parent[x])
	}
	return d.parent[x]
}

func (d *DSU) Union(x, y int) bool {
	rx, ry := d.Find(x), d.Find(y)
	if rx == ry {
		return false
	}
	if d.rank[rx] < d.rank[ry] {
		rx, ry = ry, rx
	}
	d.parent[ry] = rx
	if d.rank[rx] == d.rank[ry] {
		d.rank[rx]++
	}
	return true
}

func findRedundantConnection(edges [][]int) []int {
	n := len(edges)
	dsu := NewDSU(n)
	for _, e := range edges {
		if !dsu.Union(e[0], e[1]) {
			return e
		}
	}
	return nil
}
