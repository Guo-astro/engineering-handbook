// LC 1. Two Sum
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    seen.reserve(nums.size() * 2);  // pre-size avoids rehash during the loop
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        auto it = seen.find(complement);
        if (it != seen.end()) {
            return { it->second, i };
        }
        seen[nums[i]] = i;
    }
    return {};
}
