// LC 72. Edit Distance

class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][0] = i;     // i deletes
        for (int j = 0; j <= n; j++) dp[0][j] = j;     // j inserts
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];       // match: free diagonal
                } else {
                    dp[i][j] = 1 + Math.min(
                        dp[i - 1][j - 1],              // replace
                        Math.min(dp[i - 1][j],         // delete from word1
                                 dp[i][j - 1])         // insert into word1
                    );
                }
            }
        }
        return dp[m][n];
    }
}
