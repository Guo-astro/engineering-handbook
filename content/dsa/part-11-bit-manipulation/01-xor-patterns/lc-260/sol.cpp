// LC 260. Single Number III
//
// XOR all -> xor_all = a ^ b. Bucket by lowest differing bit. Two LC-136s.

#include <vector>
#include <cstdint>

std::vector<int> singleNumber(const std::vector<int>& nums) {
    uint32_t xorAll = 0;
    for (int x : nums) {
        xorAll ^= static_cast<uint32_t>(x);
    }
    // Use unsigned negation so the lowest-set-bit idiom is well-defined
    // even when xorAll has only the high bit set.
    uint32_t diffBit = xorAll & (0u - xorAll);
    uint32_t a = 0, b = 0;
    for (int x : nums) {
        uint32_t ux = static_cast<uint32_t>(x);
        if (ux & diffBit) {
            a ^= ux;
        } else {
            b ^= ux;
        }
    }
    return {static_cast<int>(a), static_cast<int>(b)};
}
