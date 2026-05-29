// LC 15. 3Sum
#include <algorithm>
#include <vector>

class Solution {
public:
    // LC 15. Return every unique triplet of values summing to zero.
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = static_cast<int>(nums.size());
        std::vector<std::vector<int>> out;
        for (int i = 0; i + 2 < n; ++i) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int target = -nums[i];
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                int s = nums[l] + nums[r];
                if (s < target) {
                    ++l;
                } else if (s > target) {
                    --r;
                } else {
                    out.push_back({nums[i], nums[l], nums[r]});
                    ++l;
                    --r;
                    while (l < r && nums[l] == nums[l - 1]) ++l;
                    while (l < r && nums[r] == nums[r + 1]) --r;
                }
            }
        }
        return out;
    }
};
