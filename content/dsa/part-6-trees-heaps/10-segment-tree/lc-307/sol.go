// LC 307. Range Sum Query - Mutable
package main

type NumArray struct {
	n    int
	tree []int
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	size := 4
	if n > 1 {
		size = 4 * n
	}
	na := NumArray{n: n, tree: make([]int, size)}
	if n > 0 {
		na.build(nums, 1, 0, n-1)
	}
	return na
}

func (na *NumArray) build(nums []int, v, tl, tr int) {
	if tl == tr {
		na.tree[v] = nums[tl]
		return
	}
	tm := (tl + tr) / 2
	na.build(nums, 2*v, tl, tm)
	na.build(nums, 2*v+1, tm+1, tr)
	na.tree[v] = na.tree[2*v] + na.tree[2*v+1]
}

func (na *NumArray) Update(index, val int) {
	na.updateRec(1, 0, na.n-1, index, val)
}

func (na *NumArray) updateRec(v, tl, tr, pos, newVal int) {
	if tl == tr {
		na.tree[v] = newVal
		return
	}
	tm := (tl + tr) / 2
	if pos <= tm {
		na.updateRec(2*v, tl, tm, pos, newVal)
	} else {
		na.updateRec(2*v+1, tm+1, tr, pos, newVal)
	}
	na.tree[v] = na.tree[2*v] + na.tree[2*v+1]
}

func (na *NumArray) SumRange(left, right int) int {
	return na.queryRec(1, 0, na.n-1, left, right)
}

func (na *NumArray) queryRec(v, tl, tr, l, r int) int {
	if l > r {
		return 0
	}
	if l == tl && r == tr {
		return na.tree[v]
	}
	tm := (tl + tr) / 2
	return na.queryRec(2*v, tl, tm, l, segMin(r, tm)) +
		na.queryRec(2*v+1, tm+1, tr, segMax(l, tm+1), r)
}

func segMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func segMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}
