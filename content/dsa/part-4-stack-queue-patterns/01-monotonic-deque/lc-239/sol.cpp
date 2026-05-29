// LC 239. Sliding Window Maximum
#include <deque>
#include <vector>

class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        std::deque<int> dq;  // indices; nums[dq.front()..dq.back()] strictly decreasing
        std::vector<int> out;
        out.reserve(static_cast<size_t>(nums.size()) - k + 1);
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            // ⚠️ C++: index type stays int, not size_t. The comparison
            //    dq.front <= i - k underflows for unsigned when i < k.
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }
            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }
            dq.push_back(i);
            if (i >= k - 1) {
                out.push_back(nums[dq.front()]);
            }
        }
        return out;
    }
};
