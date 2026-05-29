// LC 785. Is Graph Bipartite?
import java.util.*;

public class Sol {
    public static boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];                 // 0 = unvisited, 1 / -1 = two color classes
        for (int start = 0; start < n; start++) {
            if (color[start] != 0) continue;       // skip already-colored components
            color[start] = 1;
            Deque<Integer> q = new ArrayDeque<>(); // ArrayDeque per code-idioms.md §2.5
            q.offer(start);
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : graph[u]) {
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
