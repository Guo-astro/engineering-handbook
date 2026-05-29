// LC 5. Longest Palindromic Substring
#include <string>
#include <utility>

class Solution {
public:
    // Expand around centers: O(n^2) time, O(1) extra space.
    std::string longestPalindrome(const std::string& s) {
        if (s.empty()) return "";
        int bestL = 0, bestR = 0;
        const int n = static_cast<int>(s.length());
        for (int i = 0; i < n; ++i) {
            auto [l1, r1] = expand(s, i, i);
            auto [l2, r2] = expand(s, i, i + 1);
            if (r1 - l1 > bestR - bestL) { bestL = l1; bestR = r1; }
            if (r2 - l2 > bestR - bestL) { bestL = l2; bestR = r2; }
        }
        return s.substr(bestL, bestR - bestL + 1);
    }

private:
    std::pair<int, int> expand(const std::string& s, int left, int right) {
        while (left >= 0 && right < static_cast<int>(s.length()) && s[left] == s[right]) {
            --left;
            ++right;
        }
        return {left + 1, right - 1};
    }
};
