// LC 14. Longest Common Prefix
// Vertical scanning: walk columns of strs[0]; on first mismatch (or running
// off the end of any string), return the prefix up to that column.
// O(S) where S = sum of lengths, O(1) extra space.
#include <string>
#include <vector>

class Solution {
public:
    std::string longestCommonPrefix(const std::vector<std::string>& strs) {
        if (strs.empty()) return "";
        const std::string& first = strs[0];
        for (size_t i = 0; i < first.size(); ++i) {
            char c = first[i];
            for (size_t k = 1; k < strs.size(); ++k) {
                if (i >= strs[k].size() || strs[k][i] != c) {
                    return first.substr(0, i);
                }
            }
        }
        return first;
    }
};
