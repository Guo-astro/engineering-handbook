// LC 802. Find Eventual Safe States
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Sol {
    public static List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] revIndeg = new int[n];                // = original out-degree
        List<List<Integer>> revAdj = new ArrayList<>();
        for (int i = 0; i < n; i++) revAdj.add(new ArrayList<>());
        for (int u = 0; u < n; u++) {
            for (int v : graph[u]) {
                revAdj.get(v).add(u);                // reverse edge v -> u
                revIndeg[u]++;
            }
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int v = 0; v < n; v++) if (revIndeg[v] == 0) q.offer(v);
        boolean[] safe = new boolean[n];
        while (!q.isEmpty()) {
            int u = q.poll();
            safe[u] = true;
            for (int v : revAdj.get(u)) {
                if (--revIndeg[v] == 0) q.offer(v);
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int v = 0; v < n; v++) if (safe[v]) ans.add(v);
        return ans;
    }
}
