// LC 416. Partition Equal Subset Sum
#include <vector>

class Solution {
public:
    bool canPartition(const std::vector<int>& nums) {
        int total = 0;
        for (int x : nums) total += x;
        if (total & 1) return false;
        int target = total / 2;

        // dp[j] is true iff some subset of seen items sums exactly to j.
        std::vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int x : nums) {
            // Right-to-left so each item contributes at most once.
            for (int j = target; j >= x; --j) {
                if (dp[j - x]) dp[j] = true;
            }
            if (dp[target]) return true;
        }
        return dp[target];
    }
};
