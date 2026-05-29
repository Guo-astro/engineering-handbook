// LC 643. Maximum Average Subarray I
#include <vector>

class Solution {
public:
    // LC 643. Track the running window sum as long long; postpone the divide.
    double findMaxAverage(std::vector<int>& nums, int k) {
        long long windowSum = 0;
        for (int i = 0; i < k; ++i) {
            windowSum += nums[i];
        }
        long long bestSum = windowSum;
        for (int r = k; r < static_cast<int>(nums.size()); ++r) {
            windowSum += nums[r] - nums[r - k];
            if (windowSum > bestSum) {
                bestSum = windowSum;
            }
        }
        return static_cast<double>(bestSum) / k;
    }
};
