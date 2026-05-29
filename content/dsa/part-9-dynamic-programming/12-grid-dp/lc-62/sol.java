// LC 62. Unique Paths
public final class Sol {

    /** Full 2D table DP. dp[i][j] = dp[i-1][j] + dp[i][j-1]. */
    public static int uniquePaths2d(int m, int n) {
        int[][] dp = new int[m][n];
        for (int j = 0; j < n; j++) dp[0][j] = 1;
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }

    /** Rolling 1D row. dp[j] += dp[j-1] in place. */
    public static int uniquePaths1d(int m, int n) {
        if (m < n) { int t = m; m = n; n = t; }
        int[] dp = new int[n];
        for (int j = 0; j < n; j++) dp[j] = 1;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] = dp[j] + dp[j - 1];
            }
        }
        return dp[n - 1];
    }

    /** LeetCode-shaped public entry point. */
    public int uniquePaths(int m, int n) {
        return uniquePaths2d(m, n);
    }
}
