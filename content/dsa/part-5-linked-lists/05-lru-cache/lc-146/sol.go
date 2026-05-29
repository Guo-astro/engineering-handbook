// LC 146. LRU Cache
package main

type lruNode struct {
	key, value int
	prev, next *lruNode
}

type LRUCache struct {
	capacity   int
	cache      map[int]*lruNode
	head, tail *lruNode // sentinels: head.next = MRU; tail.prev = LRU
}

func Constructor(capacity int) LRUCache {
	head := &lruNode{}
	tail := &lruNode{}
	head.next = tail
	tail.prev = head
	return LRUCache{
		capacity: capacity,
		cache:    make(map[int]*lruNode, capacity),
		head:     head,
		tail:     tail,
	}
}

func (c *LRUCache) remove(node *lruNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (c *LRUCache) addToFront(node *lruNode) {
	node.next = c.head.next
	node.prev = c.head
	c.head.next.prev = node
	c.head.next = node
}

func (c *LRUCache) Get(key int) int {
	node, ok := c.cache[key]
	if !ok {
		return -1
	}
	c.remove(node)
	c.addToFront(node)
	return node.value
}

func (c *LRUCache) Put(key, value int) {
	if node, ok := c.cache[key]; ok {
		node.value = value
		c.remove(node)
		c.addToFront(node)
		return
	}
	if len(c.cache) == c.capacity {
		lru := c.tail.prev
		c.remove(lru)
		delete(c.cache, lru.key)
	}
	node := &lruNode{key: key, value: value}
	c.cache[key] = node
	c.addToFront(node)
}
