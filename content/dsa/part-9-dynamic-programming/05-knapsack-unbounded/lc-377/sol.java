// LC 377. Combination Sum IV
// OUTER loop = amounts; counts ordered sequences.
class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;                          // empty sequence is one valid way
        for (int a = 1; a <= target; a++) { // OUTER = amounts -> permutations
            for (int n : nums) {
                if (n <= a) {
                    dp[a] += dp[a - n];
                }
            }
        }
        return dp[target];
    }
}
