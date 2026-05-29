// LC 1971. Find if Path Exists in Graph
// Build an adjacency list from the edges, then BFS from source. Build is
// O(V + E); BFS is O(V + E). int[] visited array beats HashSet on the
// LC judge by skipping autoboxing in the hot loop.
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public final class Sol {

    public static boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) {
            return true;
        }
        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);            // undirected: push both halves
        }
        boolean[] visited = new boolean[n];
        visited[source] = true;
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(source);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (v == destination) {
                    return true;
                }
                if (!visited[v]) {
                    visited[v] = true;
                    q.offer(v);
                }
            }
        }
        return false;
    }
}
