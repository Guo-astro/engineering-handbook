// LC 1368. Minimum Cost to Make at Least One Valid Path in a Grid
import java.util.*;

public class Sol {
    public int minCost(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int[][] DIRS = {{0,0}, {0,1}, {0,-1}, {1,0}, {-1,0}};
        int[][] dist = new int[rows][cols];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;

        ArrayDeque<int[]> dq = new ArrayDeque<>();
        dq.offerFirst(new int[]{0, 0});
        while (!dq.isEmpty()) {
            int[] cell = dq.pollFirst();
            int r = cell[0], c = cell[1];
            for (int dir = 1; dir <= 4; dir++) {
                int nr = r + DIRS[dir][0], nc = c + DIRS[dir][1];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                int cost = (grid[r][c] == dir) ? 0 : 1;
                int nd = dist[r][c] + cost;
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    // 0-cost relaxations to the FRONT, 1-cost to the BACK.
                    // Reversing this is the most common 0-1 BFS bug.
                    if (cost == 0) dq.offerFirst(new int[]{nr, nc});
                    else           dq.offerLast(new int[]{nr, nc});
                }
            }
        }
        return dist[rows - 1][cols - 1];
    }
}
