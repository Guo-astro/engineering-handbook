// LC 895. Maximum Frequency Stack
// A pop returns the most-frequent element pushed so far, ties broken by
// recency. Two parallel maps: count tracks each value's current frequency;
// buckets[f] is the stack (slice) of values that have reached frequency f.
// A push at new count f appends to buckets[f] alone. A pop reads
// buckets[maxFreq] for most-frequent + most-recent in one step. O(1) per op.
package main

type FreqStack struct {
	count   map[int]int
	buckets map[int][]int
	maxFreq int
}

func Constructor() FreqStack {
	return FreqStack{
		count:   make(map[int]int),
		buckets: make(map[int][]int),
		maxFreq: 0,
	}
}

func (fs *FreqStack) Push(val int) {
	fs.count[val]++
	f := fs.count[val]
	fs.buckets[f] = append(fs.buckets[f], val)
	if f > fs.maxFreq {
		fs.maxFreq = f
	}
}

func (fs *FreqStack) Pop() int {
	bucket := fs.buckets[fs.maxFreq]
	val := bucket[len(bucket)-1]
	fs.buckets[fs.maxFreq] = bucket[:len(bucket)-1]
	fs.count[val]--
	if len(fs.buckets[fs.maxFreq]) == 0 {
		fs.maxFreq--
	}
	return val
}
