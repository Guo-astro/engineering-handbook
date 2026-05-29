// LC 743. Network Delay Time
import java.util.*;

public class Sol {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<int[]>[] adj = new List[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] e : times) adj[e[0]].add(new int[]{e[1], e[2]});

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;

        // Min-heap on dist; entries are int[]{d, u}. int[] avoids Integer
        // autoboxing on every offer/poll on this hot path (DSH-03 idiom).
        PriorityQueue<int[]> pq =
            new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, k});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (d > dist[u]) continue;                   // lazy-deletion
            for (int[] vw : adj[u]) {
                int v = vw[0], w = vw[1];
                long nd = (long) d + w;                  // overflow guard
                if (nd < dist[v]) {
                    dist[v] = (int) nd;
                    pq.offer(new int[]{(int) nd, v});
                }
            }
        }

        int longest = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            longest = Math.max(longest, dist[i]);
        }
        return longest;
    }
}
