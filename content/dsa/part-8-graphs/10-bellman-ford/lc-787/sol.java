// LC 787. Cheapest Flights Within K Stops
import java.util.Arrays;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        final int INF = Integer.MAX_VALUE;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;
        for (int i = 0; i <= k; i++) {
            // snapshot is the "previous-pass" view; without it a single pass
            // could relax a 2-edge chain, silently violating the K-edge bound.
            int[] snapshot = dist.clone();
            for (int[] f : flights) {
                int u = f[0], v = f[1], w = f[2];
                if (snapshot[u] == INF) continue;
                if (snapshot[u] + w < dist[v]) {
                    dist[v] = snapshot[u] + w;
                }
            }
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
}
