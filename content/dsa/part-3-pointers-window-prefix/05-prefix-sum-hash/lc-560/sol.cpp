// LC 560. Subarray Sum Equals K
#include <unordered_map>
#include <vector>

class Solution {
public:
    // LC 560.
    int subarraySum(std::vector<int>& nums, int k) {
        std::unordered_map<long long, int> counts;
        counts.reserve(nums.size() + 1);
        counts[0] = 1;
        long long prefix = 0;
        int answer = 0;
        long long kL = static_cast<long long>(k);
        for (int x : nums) {
            prefix += x;
            // find + iterator avoids the operator[] side-effect of inserting
            // a default-constructed entry on a missing key, which would
            // inflate the map and miscount on subsequent lookups.
            auto it = counts.find(prefix - kL);
            if (it != counts.end()) {
                answer += it->second;
            }
            ++counts[prefix];
        }
        return answer;
    }
};
