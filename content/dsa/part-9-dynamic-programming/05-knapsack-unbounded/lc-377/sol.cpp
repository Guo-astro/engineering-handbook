// LC 377. Combination Sum IV
// OUTER loop = amounts; counts ordered sequences.
#include <vector>

class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) {
        std::vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;                          // empty sequence is one valid way
        for (int a = 1; a <= target; ++a) { // OUTER = amounts -> permutations
            for (int n : nums) {
                if (n <= a) {
                    dp[a] += dp[a - n];     // intermediate values may overflow
                                            // signed 32-bit per the LC 377
                                            // follow-up; problem guarantees the
                                            // FINAL answer fits a 32-bit int.
                }
            }
        }
        return static_cast<int>(dp[target]);
    }
};
