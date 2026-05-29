// LC 174. Dungeon Game
// Backward grid DP:
//   dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
// Sentinel padding with INT_MAX so the bottom-right corner falls back to
// its own clamp; iteration is bottom-right to top-left.
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int calculateMinimumHP(std::vector<std::vector<int>>& dungeon) {
        int m = (int)dungeon.size();
        int n = (int)dungeon[0].size();
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, INT_MAX));
        dp[m][n - 1] = 1;
        dp[m - 1][n] = 1;
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                int need = std::min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                dp[i][j] = std::max(need, 1);
            }
        }
        return dp[0][0];
    }
};
