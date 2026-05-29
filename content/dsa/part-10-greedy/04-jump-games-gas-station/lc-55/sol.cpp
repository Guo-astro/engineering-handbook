// LC 55. Jump Game
// Greedy max-reach frontier sweep. O(n) time, O(1) space.
#include <vector>
#include <algorithm>

class Sol {
public:
    bool canJump(std::vector<int>& nums) {
        int maxReach = 0;
        int n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            if (i > maxReach) return false;
            maxReach = std::max(maxReach, i + nums[i]);
            if (maxReach >= n - 1) return true;
        }
        return true;
    }
};
