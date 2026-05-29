// LC 416. Partition Equal Subset Sum
class Sol {
    public static boolean canPartition(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        if ((total & 1) == 1) return false;
        int target = total / 2;

        // dp[j] is true iff some subset of seen items sums exactly to j.
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for (int x : nums) {
            // Right-to-left so each item contributes at most once.
            for (int j = target; j >= x; j--) {
                dp[j] = dp[j] || dp[j - x];
            }
            if (dp[target]) return true;
        }
        return dp[target];
    }
}
