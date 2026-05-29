// LC 933. Number of Recent Calls
package hitcounter

// RecentCounter implements LC 933's sliding-window-on-stream contract.
// Go has no native deque; the slice-as-queue idiom uses slice = slice[idx:]
// to advance the head. Production code with sustained throughput
// substitutes a ring buffer (per the code-idioms slice-front-pop footgun).
type RecentCounter struct {
	q []int
}

// Constructor returns an initialized RecentCounter.
func Constructor() RecentCounter {
	return RecentCounter{q: make([]int, 0, 16)}
}

// Ping records timestamp t and returns the count of pings in [t-3000, t].
func (rc *RecentCounter) Ping(t int) int {
	rc.q = append(rc.q, t)
	cutoff := t - 3000
	idx := 0
	// Strict `<`: rc.q[idx] == cutoff is INSIDE the window.
	for idx < len(rc.q) && rc.q[idx] < cutoff {
		idx++
	}
	if idx > 0 {
		rc.q = rc.q[idx:]
	}
	return len(rc.q)
}
