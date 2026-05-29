// LC 28. Find the Index of the First Occurrence in a String
#include <string>
#include <vector>

class Solution {
public:
    int strStr(const std::string& haystack, const std::string& needle) {
        if (needle.empty()) return 0;
        const int n = (int)haystack.size();
        const int m = (int)needle.size();
        if (m > n) return -1;
        std::vector<int> lps = computeLps(needle);
        int i = 0, j = 0;
        while (i < n) {
            if (haystack[i] == needle[j]) {
                ++i; ++j;
                if (j == m) return i - j;
            } else {
                if (j != 0) j = lps[j - 1];
                else ++i;
            }
        }
        return -1;
    }

    std::vector<int> computeLps(const std::string& pattern) {
        const int m = (int)pattern.size();
        std::vector<int> lps(m, 0);
        int length = 0, i = 1;
        while (i < m) {
            if (pattern[i] == pattern[length]) {
                ++length;
                lps[i] = length;
                ++i;
            } else {
                if (length != 0) length = lps[length - 1];
                else { lps[i] = 0; ++i; }
            }
        }
        return lps;
    }
};
