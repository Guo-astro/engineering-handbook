# LC 895. Maximum Frequency Stack
# A pop returns the most-frequent element pushed so far, breaking ties by
# recency. Carry two parallel structures: count[v] tracks v's current count;
# buckets[f] is a stack of every value that has ever reached count f. A
# push of v at new count f appends v to buckets[f] alone — earlier pushes
# placed v into buckets[1..f-1]. A pop reads buckets[max_freq], which
# returns the most-frequent value and (by stack LIFO inside the bucket)
# the most-recent among ties. O(1) per push, O(1) per pop.
from collections import defaultdict


class FreqStack:
    def __init__(self) -> None:
        self.count: dict[int, int] = defaultdict(int)
        self.buckets: dict[int, list[int]] = defaultdict(list)
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        f = self.count[val]
        self.buckets[f].append(val)
        if f > self.max_freq:
            self.max_freq = f

    def pop(self) -> int:
        val = self.buckets[self.max_freq].pop()
        self.count[val] -= 1
        if not self.buckets[self.max_freq]:
            self.max_freq -= 1
        return val
