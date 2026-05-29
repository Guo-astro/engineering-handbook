// LC 371. Sum of Two Integers

#include <cstdint>

class Solution {
public:
    int getSum(int a, int b) {
        // Use unsigned arithmetic to avoid signed-overflow UB.
        // Wrap into 32-bit unsigned; sign-bit pattern is preserved.
        uint32_t ua = static_cast<uint32_t>(a);
        uint32_t ub = static_cast<uint32_t>(b);
        while (ub != 0) {
            uint32_t carry = (ua & ub) << 1;
            ua = ua ^ ub;
            ub = carry;
        }
        return static_cast<int>(ua);
    }
};
