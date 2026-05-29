// LC 355. Design Twitter
// In-memory class with four operations. getNewsFeed runs a bounded
// k-way merge through a max-heap keyed on a monotonic timestamp; each
// author contributes at most one heap entry at a time, so heap size
// stays at |followees| + 1. PriorityQueue<int[]> avoids autoboxing
// in the comparator hot path; the comparator uses Integer.compare(b, a)
// for max-heap semantics without subtraction-overflow risk.
import java.util.*;

public class Twitter {
    private static final int FEED_CAP = 10;

    private final Map<Integer, List<int[]>> tweets = new HashMap<>();      // userId -> list of {ts, tweetId}
    private final Map<Integer, Set<Integer>> following = new HashMap<>();  // userId -> followees
    private int ts = 0;

    public Twitter() {}

    public void postTweet(int userId, int tweetId) {
        ts++;
        tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new int[]{ts, tweetId});
    }

    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> authors = new HashSet<>(following.getOrDefault(userId, Collections.emptySet()));
        authors.add(userId);

        // Max-heap on ts. Entry: [ts, tweetId, authorId, idxInTheirList].
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        for (int a : authors) {
            List<int[]> tw = tweets.get(a);
            if (tw == null || tw.isEmpty()) continue;
            int idx = tw.size() - 1;
            int[] last = tw.get(idx);
            heap.offer(new int[]{last[0], last[1], a, idx});
        }

        List<Integer> feed = new ArrayList<>(FEED_CAP);
        while (!heap.isEmpty() && feed.size() < FEED_CAP) {
            int[] top = heap.poll();
            feed.add(top[1]);
            int a = top[2];
            int idx = top[3];
            if (idx > 0) {
                int next = idx - 1;
                int[] prev = tweets.get(a).get(next);
                // Allocate a fresh array on push; never mutate one already in the heap.
                heap.offer(new int[]{prev[0], prev[1], a, next});
            }
        }
        return feed;
    }

    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        following.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        Set<Integer> s = following.get(followerId);
        if (s != null) s.remove(followeeId);
    }
}
