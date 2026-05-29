// LC 1584. Min Cost to Connect All Points
import java.util.PriorityQueue;

class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        if (n <= 1) return 0;
        boolean[] inMst = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[]{0, 0});         // (weight, vertex)
        int total = 0;
        int edgesAdded = 0;
        while (!pq.isEmpty() && edgesAdded < n) {
            int[] top = pq.poll();
            int w = top[0], u = top[1];
            if (inMst[u]) continue;        // stale entry
            inMst[u] = true;
            total += w;
            edgesAdded++;
            for (int v = 0; v < n; v++) {
                if (!inMst[v]) {
                    int d = Math.abs(points[u][0] - points[v][0])
                          + Math.abs(points[u][1] - points[v][1]);
                    pq.offer(new int[]{d, v});
                }
            }
        }
        return total;
    }
}
