// LC 312. Burst Balloons
//
// LC 312 constraints: n <= 300, 0 <= nums[i] <= 100. Max single-burst gain
// is 100^3 = 1e6; total over all bursts < 3e8, well below INT_MAX. 32-bit
// int is sufficient (no long long promotion needed).
#include <vector>

class Solution {
public:
    // LC 312.
    int maxCoins(std::vector<int>& nums) {
        int m = static_cast<int>(nums.size());
        std::vector<int> a;
        a.reserve(m + 2);
        a.push_back(1);
        for (int x : nums) {
            a.push_back(x);
        }
        a.push_back(1);
        int n = static_cast<int>(a.size());
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int length = 2; length < n; ++length) {
            for (int i = 0; i + length < n; ++i) {
                int j = i + length;
                int best = 0;
                // k = LAST balloon to burst inside (i, j).
                for (int k = i + 1; k < j; ++k) {
                    int gain = a[i] * a[k] * a[j] + dp[i][k] + dp[k][j];
                    if (gain > best) {
                        best = gain;
                    }
                }
                dp[i][j] = best;
            }
        }
        return dp[0][n - 1];
    }
};
