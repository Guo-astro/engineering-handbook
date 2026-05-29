// LC 198. House Robber
#include <vector>
#include <algorithm>

class Solution {
public:
    int rob(const std::vector<int>& nums) {
        int prev2 = 0, prev1 = 0;
        for (int x : nums) {
            int cur = std::max(prev1, prev2 + x);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
};
