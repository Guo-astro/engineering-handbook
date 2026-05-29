// LC 355. Design Twitter
// In-memory class with four operations. getNewsFeed runs a bounded
// k-way merge through a max-heap keyed on a monotonic timestamp.
// container/heap requires implementing heap.Interface (5 methods);
// flipping Less from < to > converts the default min-heap to a max-heap.
package main

import "container/heap"

const feedCap = 10

type tweet struct {
	ts      int
	tweetID int
}

type heapItem struct {
	ts       int
	tweetID  int
	authorID int
	idx      int
}

// Max-heap on ts: Less returns h[i].ts > h[j].ts.
type tweetHeap []heapItem

func (h tweetHeap) Len() int           { return len(h) }
func (h tweetHeap) Less(i, j int) bool { return h[i].ts > h[j].ts }
func (h tweetHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *tweetHeap) Push(x any)        { *h = append(*h, x.(heapItem)) }
func (h *tweetHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type Twitter struct {
	tweets    map[int][]tweet
	following map[int]map[int]struct{}
	ts        int
}

func Constructor() Twitter {
	return Twitter{
		tweets:    make(map[int][]tweet),
		following: make(map[int]map[int]struct{}),
	}
}

func (t *Twitter) PostTweet(userID, tweetID int) {
	t.ts++
	t.tweets[userID] = append(t.tweets[userID], tweet{ts: t.ts, tweetID: tweetID})
}

func (t *Twitter) GetNewsFeed(userID int) []int {
	authors := map[int]struct{}{userID: {}}
	for a := range t.following[userID] {
		authors[a] = struct{}{}
	}
	h := &tweetHeap{}
	for a := range authors {
		tw := t.tweets[a]
		if len(tw) == 0 {
			continue
		}
		idx := len(tw) - 1
		heap.Push(h, heapItem{ts: tw[idx].ts, tweetID: tw[idx].tweetID, authorID: a, idx: idx})
	}
	feed := make([]int, 0, feedCap)
	for h.Len() > 0 && len(feed) < feedCap {
		top := heap.Pop(h).(heapItem)
		feed = append(feed, top.tweetID)
		if top.idx > 0 {
			next := top.idx - 1
			tw := t.tweets[top.authorID][next]
			heap.Push(h, heapItem{ts: tw.ts, tweetID: tw.tweetID, authorID: top.authorID, idx: next})
		}
	}
	return feed
}

func (t *Twitter) Follow(followerID, followeeID int) {
	if followerID == followeeID {
		return
	}
	if _, ok := t.following[followerID]; !ok {
		t.following[followerID] = make(map[int]struct{})
	}
	t.following[followerID][followeeID] = struct{}{}
}

func (t *Twitter) Unfollow(followerID, followeeID int) {
	if s, ok := t.following[followerID]; ok {
		delete(s, followeeID)
	}
}
