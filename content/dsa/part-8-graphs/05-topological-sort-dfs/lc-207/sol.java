// LC 207. Course Schedule
import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int WHITE = 0, GRAY = 1, BLACK = 2;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] e : prerequisites) {
            int a = e[0], b = e[1]; // b -> a
            adj.get(b).add(a);
        }
        int[] color = new int[numCourses];
        for (int u = 0; u < numCourses; u++) {
            if (color[u] == WHITE && !dfs(u, adj, color)) return false;
        }
        return true;
    }

    private boolean dfs(int u, List<List<Integer>> adj, int[] color) {
        color[u] = GRAY;
        for (int v : adj.get(u)) {
            if (color[v] == GRAY) return false;       // back edge
            if (color[v] == WHITE && !dfs(v, adj, color)) return false;
        }
        color[u] = BLACK;                              // post-order point
        return true;
    }
}
