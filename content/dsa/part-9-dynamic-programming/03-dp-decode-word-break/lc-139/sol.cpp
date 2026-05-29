// LC 139. Word Break

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Sol {
public:
    bool wordBreak(const std::string& s,
                   const std::vector<std::string>& wordDict) {
        const int n = static_cast<int>(s.size());
        std::unordered_set<std::string> words(wordDict.begin(), wordDict.end());
        int maxW = 0;
        for (const auto& w : words)
            maxW = std::max(maxW, static_cast<int>(w.size()));
        std::vector<bool> dp(n + 1, false);
        dp[0] = true;
        for (int i = 1; i <= n; ++i) {
            int lo = std::max(0, i - maxW);
            for (int j = lo; j < i; ++j) {
                if (dp[j] && words.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};
