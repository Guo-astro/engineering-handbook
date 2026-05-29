// LC 312. Burst Balloons
public final class Sol {

    // LC 312.
    public static int maxCoins(int[] nums) {
        int m = nums.length;
        int[] a = new int[m + 2];
        a[0] = 1;
        a[m + 1] = 1;
        for (int i = 0; i < m; i++) {
            a[i + 1] = nums[i];
        }
        int n = m + 2;
        int[][] dp = new int[n][n];
        // Length-major fill: every smaller subproblem is computed before
        // the cell that depends on it.
        for (int length = 2; length < n; length++) {
            for (int i = 0; i + length < n; i++) {
                int j = i + length;
                int best = 0;
                // k = LAST balloon to burst inside (i, j); its neighbors at
                // pop time are guaranteed to be a[i] and a[j].
                for (int k = i + 1; k < j; k++) {
                    int gain = a[i] * a[k] * a[j] + dp[i][k] + dp[k][j];
                    if (gain > best) {
                        best = gain;
                    }
                }
                dp[i][j] = best;
            }
        }
        return dp[0][n - 1];
    }

    private Sol() {}
}
