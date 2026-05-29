// LC 210. Course Schedule II
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Sol {
    public static int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] indeg = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] e : prerequisites) {
            int a = e[0], b = e[1]; // b -> a
            adj.get(b).add(a);
            indeg[a]++;
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int v = 0; v < numCourses; v++) if (indeg[v] == 0) q.offer(v);
        int[] order = new int[numCourses];
        int idx = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            order[idx++] = u;
            for (int v : adj.get(u)) {
                if (--indeg[v] == 0) q.offer(v);
            }
        }
        return idx == numCourses ? order : new int[0];
    }
}
