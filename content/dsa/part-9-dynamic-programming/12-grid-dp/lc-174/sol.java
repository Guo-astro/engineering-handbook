// LC 174. Dungeon Game
// Backward grid DP:
//   dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
// Sentinel padding with Integer.MAX_VALUE so the bottom-right corner falls
// back to its own clamp; iteration is bottom-right to top-left.
public final class Sol {

    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                dp[i][j] = Math.max(need, 1);
            }
        }
        return dp[0][0];
    }
}
