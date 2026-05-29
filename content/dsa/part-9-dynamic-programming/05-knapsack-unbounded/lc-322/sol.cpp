// LC 322. Coin Change
#include <vector>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        const int INF = amount + 1;
        std::vector<int> dp(amount + 1, INF);
        dp[0] = 0;
        for (int a = 1; a <= amount; ++a) {
            for (int c : coins) {
                if (c <= a && dp[a - c] + 1 < dp[a]) {
                    dp[a] = dp[a - c] + 1;
                }
            }
        }
        return dp[amount] >= INF ? -1 : dp[amount];
    }
};
