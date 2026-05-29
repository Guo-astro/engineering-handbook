// LC 1584. Min Cost to Connect All Points
import java.util.Arrays;

public class Sol {
    static int[] parent;
    static int[] rank_;

    static int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]]; // path halving
            x = parent[x];
        }
        return x;
    }

    static boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (rank_[ra] < rank_[rb]) { int t = ra; ra = rb; rb = t; }
        parent[rb] = ra;
        if (rank_[ra] == rank_[rb]) rank_[ra]++;
        return true;
    }

    public static int minCostConnectPoints(int[][] points) {
        int n = points.length;
        if (n <= 1) return 0;
        int[][] edges = new int[n * (n - 1) / 2][3]; // {w, u, v}
        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int w = Math.abs(points[i][0] - points[j][0])
                      + Math.abs(points[i][1] - points[j][1]);
                edges[idx++] = new int[] {w, i, j};
            }
        }
        Arrays.sort(edges, (a, b) -> Integer.compare(a[0], b[0]));
        parent = new int[n];
        rank_ = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        long total = 0;             // long accumulator: sum can exceed Integer.MAX_VALUE
        int accepted = 0;
        for (int[] e : edges) {
            if (union(e[1], e[2])) {
                total += e[0];
                if (++accepted == n - 1) break;
            }
        }
        return (int) total;
    }
}
