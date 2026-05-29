// LC 547. Number of Provinces
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                bfs(isConnected, visited, i, n);
            }
        }
        return count;
    }

    private void bfs(int[][] isConnected, boolean[] visited, int start, int n) {
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v = 0; v < n; v++) {
                if (isConnected[u][v] == 1 && !visited[v]) {
                    visited[v] = true;
                    q.offer(v);
                }
            }
        }
    }
}
