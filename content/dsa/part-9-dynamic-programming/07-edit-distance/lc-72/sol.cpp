// LC 72. Edit Distance

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minDistance(const std::string& word1, const std::string& word2) {
        int m = static_cast<int>(word1.size());
        int n = static_cast<int>(word2.size());
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 0; i <= m; ++i) dp[i][0] = i;     // i deletes
        for (int j = 0; j <= n; ++j) dp[0][j] = j;     // j inserts
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];       // match: free diagonal
                } else {
                    dp[i][j] = 1 + std::min({
                        dp[i - 1][j - 1],              // replace
                        dp[i - 1][j],                  // delete from word1
                        dp[i][j - 1]                   // insert into word1
                    });
                }
            }
        }
        return dp[m][n];
    }
};
