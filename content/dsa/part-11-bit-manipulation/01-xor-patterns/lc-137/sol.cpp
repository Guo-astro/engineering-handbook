// LC 137. Single Number II
//
// Per-bit count modulo 3: O(32n) = O(n) time, O(1) space.

#include <vector>
#include <cstdint>

int singleNumber(const std::vector<int>& nums) {
    uint32_t result = 0;
    for (int i = 0; i < 32; ++i) {
        int bitSum = 0;
        for (int x : nums) {
            bitSum += (static_cast<uint32_t>(x) >> i) & 1u;
        }
        if (bitSum % 3 != 0) {
            result |= 1u << i;
        }
    }
    return static_cast<int>(result);
}
