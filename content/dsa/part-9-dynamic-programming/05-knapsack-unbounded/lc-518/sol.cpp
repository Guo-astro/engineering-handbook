// LC 518. Coin Change II
// OUTER loop = coins is mandatory; counts unordered combinations.
#include <vector>

class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        std::vector<unsigned int> dp(amount + 1, 0);
        dp[0] = 1;                          // empty multiset is one valid way
        for (int c : coins) {               // OUTER = coins -> combinations
            for (int a = c; a <= amount; ++a) {
                dp[a] += dp[a - c];         // unsigned silences UB warnings on
                                            // intermediate overflow; final
                                            // answer is guaranteed to fit
                                            // signed 32-bit per LC 518.
            }
        }
        return static_cast<int>(dp[amount]);
    }
};
