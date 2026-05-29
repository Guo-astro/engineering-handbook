// LC 886. Possible Bipartition
// Build adjacency from 1-indexed dislikes, then run standard 2-coloring BFS.
import java.util.*;

public class Sol {
    public static boolean possibleBipartition(int n, int[][] dislikes) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>()); // 1-indexed; slot 0 unused
        for (int[] d : dislikes) {
            graph.get(d[0]).add(d[1]);
            graph.get(d[1]).add(d[0]);
        }

        int[] color = new int[n + 1];                 // 0 = unvisited, 1 / -1 = two groups
        for (int start = 1; start <= n; start++) {
            if (color[start] != 0) continue;
            color[start] = 1;
            Deque<Integer> q = new ArrayDeque<>();
            q.offer(start);
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : graph.get(u)) {
                    if (color[v] == 0) {
                        color[v] = -color[u];
                        q.offer(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
