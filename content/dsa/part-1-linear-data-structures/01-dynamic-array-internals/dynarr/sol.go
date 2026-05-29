// DynArr — geometric-resize dynamic array reference template.
// Parameterized growth factor (growthNum / growthDen) for studying the
// amortized-O(1) push proof; tracks reallocation count. Not an LC problem.
package main

import "errors"

type DynArr[T any] struct {
	buf       []T
	size      int
	cap       int
	growthNum int
	growthDen int
	reallocs  int
}

func NewDynArr[T any](initialCap, growthNum, growthDen int) (*DynArr[T], error) {
	if initialCap < 1 {
		return nil, errors.New("initialCap must be >= 1")
	}
	if growthNum <= growthDen {
		return nil, errors.New("growth factor must be > 1")
	}
	return &DynArr[T]{
		buf:       make([]T, initialCap),
		size:      0,
		cap:       initialCap,
		growthNum: growthNum,
		growthDen: growthDen,
	}, nil
}

func (a *DynArr[T]) Size() int          { return a.size }
func (a *DynArr[T]) Capacity() int      { return a.cap }
func (a *DynArr[T]) Reallocations() int { return a.reallocs }

func (a *DynArr[T]) Get(i int) (T, error) {
	var zero T
	if i < 0 || i >= a.size {
		return zero, errors.New("get out of range")
	}
	return a.buf[i], nil
}

func (a *DynArr[T]) Push(x T) {
	if a.size == a.cap {
		a.grow()
	}
	a.buf[a.size] = x
	a.size += 1
}

func (a *DynArr[T]) grow() {
	// Ceiling division so factors like 9/8 still grow on small caps.
	newCap := (a.cap*a.growthNum + a.growthDen - 1) / a.growthDen
	// Guard against rounding to a no-op (would loop forever on next push).
	if newCap <= a.cap {
		newCap = a.cap + 1
	}
	newBuf := make([]T, newCap)
	copy(newBuf, a.buf[:a.size])
	a.buf = newBuf
	a.cap = newCap
	a.reallocs += 1
}
