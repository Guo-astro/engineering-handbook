# LC 460. LFU Cache
from collections import defaultdict, OrderedDict


class LFUCache:
    """LFU cache with O(1) get/put using a freq-bucket of OrderedDicts.
    Tie-break inside a freq bucket = LRU (oldest insertion wins eviction)."""

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.min_freq = 0
        # key -> [val, freq]; list (mutable) so we can update freq in place.
        self.kvf = {}
        # freq -> OrderedDict[key] = None; insertion order = LRU within bucket.
        self.fk = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.kvf:
            return -1
        val, freq = self.kvf[key]
        del self.fk[freq][key]
        if not self.fk[freq]:
            del self.fk[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.fk[freq + 1][key] = None
        self.kvf[key] = [val, freq + 1]
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.kvf:
            self.kvf[key][0] = value
            self.get(key)  # reuse promotion logic
            return
        if self.size == self.cap:
            evict_key, _ = self.fk[self.min_freq].popitem(last=False)
            if not self.fk[self.min_freq]:
                del self.fk[self.min_freq]
            del self.kvf[evict_key]
            self.size -= 1
        self.kvf[key] = [value, 1]
        self.fk[1][key] = None
        self.min_freq = 1
        self.size += 1
