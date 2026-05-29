// LC 28. Find the Index of the First Occurrence in a String
#include <string>
#include <cstdint>

class Solution {
public:
    int strStr(const std::string& haystack, const std::string& needle) {
        const int n = static_cast<int>(haystack.size());
        const int m = static_cast<int>(needle.size());
        if (m == 0) return 0;
        if (m > n)  return -1;

        // uint64_t for products: avoids signed-overflow UB and gives a
        // 64-bit wraparound modulus that is always well-defined.
        const uint64_t base = 256ULL;
        const uint64_t mod  = 1000000007ULL;

        uint64_t high_power = 1ULL;
        for (int i = 0; i < m - 1; ++i) {
            high_power = (high_power * base) % mod;
        }

        uint64_t needle_hash = 0ULL, window_hash = 0ULL;
        for (int i = 0; i < m; ++i) {
            needle_hash = (needle_hash * base + (uint8_t)needle[i])   % mod;
            window_hash = (window_hash * base + (uint8_t)haystack[i]) % mod;
        }

        for (int i = 0; i <= n - m; ++i) {
            if (window_hash == needle_hash
                    && haystack.compare(i, m, needle) == 0) {
                return i;
            }
            if (i < n - m) {
                uint64_t leading = ((uint8_t)haystack[i] * high_power) % mod;
                window_hash = (window_hash + mod - leading) % mod;
                window_hash = (window_hash * base
                               + (uint8_t)haystack[i + m]) % mod;
            }
        }
        return -1;
    }
};
