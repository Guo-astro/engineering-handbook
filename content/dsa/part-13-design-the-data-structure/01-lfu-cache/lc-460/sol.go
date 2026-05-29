// LC 460. LFU Cache
package main

import "container/list"

type LFUCache struct {
	cap, size, minFreq int
	keyMap             map[int]*entry
	freqMap            map[int]*list.List
}

type entry struct {
	key, val, freq int
	elem           *list.Element
}

func Constructor(capacity int) LFUCache {
	return LFUCache{
		cap:     capacity,
		keyMap:  make(map[int]*entry),
		freqMap: make(map[int]*list.List),
	}
}

func (c *LFUCache) Get(key int) int {
	e, ok := c.keyMap[key]
	if !ok {
		return -1
	}
	c.promote(e)
	return e.val
}

func (c *LFUCache) Put(key int, value int) {
	if c.cap <= 0 {
		return
	}
	if e, ok := c.keyMap[key]; ok {
		e.val = value
		c.promote(e)
		return
	}
	if c.size == c.cap {
		bucket := c.freqMap[c.minFreq]
		front := bucket.Front()
		evict := front.Value.(*entry)
		bucket.Remove(front)
		if bucket.Len() == 0 {
			delete(c.freqMap, c.minFreq)
		}
		delete(c.keyMap, evict.key)
		c.size--
	}
	e := &entry{key: key, val: value, freq: 1}
	if _, ok := c.freqMap[1]; !ok {
		c.freqMap[1] = list.New()
	}
	e.elem = c.freqMap[1].PushBack(e)
	c.keyMap[key] = e
	c.minFreq = 1
	c.size++
}

func (c *LFUCache) promote(e *entry) {
	cur := c.freqMap[e.freq]
	cur.Remove(e.elem)
	if cur.Len() == 0 {
		delete(c.freqMap, e.freq)
		if c.minFreq == e.freq {
			c.minFreq++
		}
	}
	e.freq++
	if _, ok := c.freqMap[e.freq]; !ok {
		c.freqMap[e.freq] = list.New()
	}
	e.elem = c.freqMap[e.freq].PushBack(e)
}
