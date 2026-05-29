// LC 136. Single Number

#include <vector>

// Pair-cancel reduction. O(n) time, O(1) space.
int singleNumber(const std::vector<int>& nums) {
    int result = 0;
    for (int x : nums) {
        result ^= x;
    }
    return result;
}
