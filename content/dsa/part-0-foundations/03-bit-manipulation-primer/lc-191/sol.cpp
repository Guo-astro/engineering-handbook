// LC 191. Number of 1 Bits

#include <cstdint>

// Brian Kernighan's loop. O(popcount(n)) time, O(1) space.
int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) {
        n &= n - 1; // clear the lowest set bit
        ++count;
    }
    return count;
}
