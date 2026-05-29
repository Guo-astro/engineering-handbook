// LC 300. Longest Increasing Subsequence
#include <algorithm>
#include <vector>

class Solution {
public:
    int lengthOfLIS(const std::vector<int>& nums) {
        const int n = static_cast<int>(nums.size());
        if (n == 0) return 0;
        std::vector<int> dp(n, 1);
        int best = 1;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i] && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                }
            }
            if (dp[i] > best) best = dp[i];
        }
        return best;
    }
};
