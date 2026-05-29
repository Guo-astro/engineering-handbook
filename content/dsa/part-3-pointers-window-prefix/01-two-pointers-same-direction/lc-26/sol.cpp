// LC 26. Remove Duplicates from Sorted Array
#include <vector>

class Solution {
public:
    /**
     * LC 26: Remove duplicates from a sorted array in-place; return new length k.
     * Invariant: nums[0..write) is a sorted prefix of distinct elements.
     */
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int write = 1;
        for (int read = 1; read < static_cast<int>(nums.size()); ++read) {
            if (nums[read] != nums[write - 1]) {
                nums[write] = nums[read];
                ++write;
            }
        }
        return write;
    }
};
