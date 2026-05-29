// LC 5. Longest Palindromic Substring
#include <string>
#include <vector>

class Solution {
public:
    // Approach A: 2D DP by-length. O(n^2) time, O(n^2) space.
    std::string longestPalindrome(const std::string& s) {
        int n = static_cast<int>(s.length());
        if (n == 0) return "";
        std::vector<std::vector<bool>> isPalin(n, std::vector<bool>(n, false));
        int start = 0, maxLen = 1;

        // Length 1.
        for (int i = 0; i < n; ++i) isPalin[i][i] = true;

        // Length 2.
        for (int i = 0; i + 1 < n; ++i) {
            if (s[i] == s[i + 1]) {
                isPalin[i][i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }

        // Length L from 3 to n.
        for (int L = 3; L <= n; ++L) {
            for (int i = 0; i + L - 1 < n; ++i) {
                int j = i + L - 1;
                if (s[i] == s[j] && isPalin[i + 1][j - 1]) {
                    isPalin[i][j] = true;
                    if (L > maxLen) {
                        start = i;
                        maxLen = L;
                    }
                }
            }
        }
        return s.substr(start, maxLen);
    }

    // Approach B: expand around centers. O(n^2) time, O(1) space.
    std::string longestPalindromeCenters(const std::string& s) {
        if (s.empty()) return "";
        int bestL = 0, bestR = 0;
        for (int i = 0; i < static_cast<int>(s.length()); ++i) {
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
