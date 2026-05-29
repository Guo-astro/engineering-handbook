// LC 213. House Robber II
#include <vector>
#include <algorithm>

class Sol {
public:
    // LC 213 House Robber II. Circular -> two linear sub-ranges, max of both.
    int rob(const std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return std::max(nums[0], nums[1]);
        return std::max(robLinear(nums, 0, n - 2),
                        robLinear(nums, 1, n - 1));
    }

private:
    // Linear House Robber on nums[lo..hi] inclusive. O(1) space.
    int robLinear(const std::vector<int>& nums, int lo, int hi) {
        int prev2 = 0, prev1 = 0;
        for (int i = lo; i <= hi; ++i) {
            int curr = std::max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};
