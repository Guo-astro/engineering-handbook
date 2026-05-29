// LC 1143. Longest Common Subsequence
#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int longestCommonSubsequence(const std::string& text1, const std::string& text2) {
        int m = static_cast<int>(text1.size());
        int n = static_cast<int>(text2.size());
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }

    /** Recover the LCS string by backtracking from (m, n) per CLRS 14.4 PRINT-LCS. */
    std::string lcsString(const std::string& text1, const std::string& text2) {
        int m = static_cast<int>(text1.size());
        int n = static_cast<int>(text2.size());
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        std::string out;
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (text1[i - 1] == text2[j - 1]) {
                out.push_back(text1[i - 1]);
                --i; --j;
            } else if (dp[i - 1][j] >= dp[i][j - 1]) {
                --i;
            } else {
                --j;
            }
        }
        std::reverse(out.begin(), out.end());
        return out;
    }

    /** Length-only space-optimized form. Two rolling rows of size min(m, n) + 1. */
    int longestCommonSubsequenceRolling(std::string text1, std::string text2) {
        if (text1.size() < text2.size()) std::swap(text1, text2);
        int m = static_cast<int>(text1.size());
        int n = static_cast<int>(text2.size());
        std::vector<int> prev(n + 1, 0);
        std::vector<int> curr(n + 1, 0);
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) {
                    curr[j] = prev[j - 1] + 1;
                } else {
                    curr[j] = std::max(prev[j], curr[j - 1]);
                }
            }
            std::swap(prev, curr);
            std::fill(curr.begin(), curr.end(), 0);
        }
        return prev[n];
    }
};
