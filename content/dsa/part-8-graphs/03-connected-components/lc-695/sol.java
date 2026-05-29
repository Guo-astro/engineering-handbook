// LC 695. Max Area of Island
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {
    private static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int maxAreaOfIsland(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int rows = grid.length, cols = grid[0].length;
        int best = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    int area = bfs(grid, r, c, rows, cols);
                    if (area > best) best = area;
                }
            }
        }
        return best;
    }

    private int bfs(int[][] grid, int sr, int sc, int rows, int cols) {
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{sr, sc});
        grid[sr][sc] = 0;
        int size = 0;
        while (!q.isEmpty()) {
            int[] cell = q.poll();
            size++;
            for (int[] d : DIRS) {
                int nr = cell[0] + d[0], nc = cell[1] + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 0;
                    q.offer(new int[]{nr, nc});
                }
            }
        }
        return size;
    }
}
