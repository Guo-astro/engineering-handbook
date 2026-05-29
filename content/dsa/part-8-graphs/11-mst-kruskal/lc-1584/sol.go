// LC 1584. Min Cost to Connect All Points
package main

import "sort"

type dsu struct {
	parent []int
	rank   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	for i := range p {
		p[i] = i
	}
	return &dsu{parent: p, rank: make([]int, n)}
}

func (d *dsu) find(x int) int {
	for d.parent[x] != x {
		d.parent[x] = d.parent[d.parent[x]]
		x = d.parent[x]
	}
	return x
}

func (d *dsu) union(a, b int) bool {
	ra, rb := d.find(a), d.find(b)
	if ra == rb {
		return false
	}
	if d.rank[ra] < d.rank[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	if d.rank[ra] == d.rank[rb] {
		d.rank[ra]++
	}
	return true
}

func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

type edge struct{ w, u, v int }

func minCostConnectPoints(points [][]int) int {
	n := len(points)
	if n <= 1 {
		return 0
	}
	edges := make([]edge, 0, n*(n-1)/2)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			w := absInt(points[i][0]-points[j][0]) + absInt(points[i][1]-points[j][1])
			edges = append(edges, edge{w, i, j})
		}
	}
	sort.Slice(edges, func(a, b int) bool { return edges[a].w < edges[b].w })
	d := newDSU(n)
	total, accepted := 0, 0
	for _, e := range edges {
		if d.union(e.u, e.v) {
			total += e.w
			accepted++
			if accepted == n-1 {
				break
			}
		}
	}
	return total
}
