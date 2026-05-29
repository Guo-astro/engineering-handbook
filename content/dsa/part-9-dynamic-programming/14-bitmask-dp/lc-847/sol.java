// LC 847. Shortest Path Visiting All Nodes
// Bitmask BFS over (node, mask) states. n <= 12; state space n * 2^n
// fits a 12 * 4096 boolean[][] comfortably.
import java.util.ArrayDeque;
import java.util.Deque;

public class Sol {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        if (n == 1) return 0;
        int fullMask = (1 << n) - 1;

        boolean[][] visited = new boolean[n][1 << n];
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            int startMask = 1 << i;
            visited[i][startMask] = true;
            queue.add(new int[]{i, startMask, 0});
        }

        while (!queue.isEmpty()) {
            int[] s = queue.poll();
            int node = s[0], mask = s[1], dist = s[2];
            if (mask == fullMask) return dist;
            for (int nb : graph[node]) {
                int newMask = mask | (1 << nb);
                if (!visited[nb][newMask]) {
                    visited[nb][newMask] = true;
                    queue.add(new int[]{nb, newMask, dist + 1});
                }
            }
        }

        return -1; // LC constraints guarantee connectivity; defensive.
    }
}
