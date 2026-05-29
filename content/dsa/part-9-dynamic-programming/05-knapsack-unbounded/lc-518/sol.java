// LC 518. Coin Change II
// OUTER loop = coins is mandatory; counts unordered combinations.
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;                          // empty multiset is one valid way
        for (int c : coins) {               // OUTER = coins -> combinations
            for (int a = c; a <= amount; a++) {
                dp[a] += dp[a - c];
            }
        }
        return dp[amount];
    }
}
