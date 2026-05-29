// LC 28. Find the Index of the First Occurrence in a String
#include <string>

class Solution {
public:
    int strStr(const std::string& haystack, const std::string& needle) {
        int n = static_cast<int>(haystack.size());
        int m = static_cast<int>(needle.size());
        if (m == 0) return 0;
        if (m > n) return -1;
        for (int i = 0; i <= n - m; ++i) {
            int j = 0;
            while (j < m && haystack[i + j] == needle[j]) {
                ++j;
            }
            if (j == m) return i;
        }
        return -1;
    }
};
