# LC 355. Design Twitter
# In-memory class with four operations. The non-trivial work is in
# getNewsFeed, which k-way-merges per-author tweet logs through a max-heap
# keyed on a monotonic timestamp. Heap size is bounded by the author count,
# not the total tweet count, because each author contributes one entry at a
# time. O(k log k) per call where k = |followees| + 1; O(1) for the others.
import heapq
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Twitter:
    """In-memory Twitter timeline supporting post/follow/unfollow/news-feed."""

    FEED_CAP = 10

    def __init__(self) -> None:
        self.tweets: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.following: Dict[int, Set[int]] = defaultdict(set)
        self.ts: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ts += 1
        self.tweets[userId].append((self.ts, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        authors = self.following[userId] | {userId}
        # heapq is min-only; negate ts to simulate a max-heap.
        heap: List[Tuple[int, int, int, int]] = []
        for a in authors:
            tw = self.tweets.get(a)
            if not tw:
                continue
            idx = len(tw) - 1
            ts, tid = tw[idx]
            heapq.heappush(heap, (-ts, tid, a, idx))

        feed: List[int] = []
        while heap and len(feed) < self.FEED_CAP:
            _, tid, a, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                next_idx = idx - 1
                nts, ntid = self.tweets[a][next_idx]
                heapq.heappush(heap, (-nts, ntid, a, next_idx))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
