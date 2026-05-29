// LC 1. Two Sum
// One pass with a value -> first-seen-index map. Look up the complement
// BEFORE inserting; the lookup-then-insert order prevents matching an
// element against itself on inputs like [3, 3]. O(n) time, O(n) space.
//
// reserve before the loop avoids rehashing on the way up; not required
// for correctness but cuts allocator churn on adversarial inputs.
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    seen.reserve(nums.size() * 2);
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
