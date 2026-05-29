# LC 362. Design Hit Counter (Premium)
# Note: LC 362 is Premium and was NOT directly fetched during research; the
# design below mirrors the standard 300-bucket array solution per research
# §3.2 and §5.2, which was cross-referenced via the Premium-equivalent map.


class HitCounter:
    """LC 362 — bucket-array hit counter, fixed memory.

    The window is W = 300 seconds. We pre-allocate 300 slots indexed by
    `t % 300`; each slot stores (bucket_timestamp, count). On hit(t), if
    the slot's stamp is `t`, increment; otherwise overwrite with (t, 1).
    On getHits(t), sum every slot whose stamp is within the last 300s.

    hit:     O(1)
    getHits: O(W) = O(300), constant in W.
    space:   O(W) = O(300).
    """

    def __init__(self) -> None:
        self.W = 300
        self.times = [0] * self.W
        self.counts = [0] * self.W

    def hit(self, t: int) -> None:
        idx = t % self.W
        if self.times[idx] == t:
            self.counts[idx] += 1
        else:
            # The slot's old stamp is outside the current window; reset.
            self.times[idx] = t
            self.counts[idx] = 1

    def getHits(self, t: int) -> int:
        cutoff = t - self.W
        total = 0
        for i in range(self.W):
            # Strict `>`: a bucket stamped exactly at `cutoff` is OUTSIDE
            # the inclusive [cutoff + 1, t] window LC 362 uses.
            if self.times[i] > cutoff:
                total += self.counts[i]
        return total
