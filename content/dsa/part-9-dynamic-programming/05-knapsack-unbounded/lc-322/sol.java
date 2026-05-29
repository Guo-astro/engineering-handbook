// LC 322. Coin Change
import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
        int INF = amount + 1;                // safe sentinel; > any real answer
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for (int a = 1; a <= amount; a++) {
            for (int c : coins) {
                if (c <= a && dp[a - c] + 1 < dp[a]) {
                    dp[a] = dp[a - c] + 1;
                }
            }
        }
        return dp[amount] >= INF ? -1 : dp[amount];
    }
}
