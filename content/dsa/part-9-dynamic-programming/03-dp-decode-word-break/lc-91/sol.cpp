// LC 91. Decode Ways

#include <string>

class Sol {
public:
    int numDecodings(const std::string& s) {
        const int n = static_cast<int>(s.size());
        if (n == 0 || s[0] == '0') return 0;
        // Rolling window: prev2 = dp[i-2], prev1 = dp[i-1].
        int prev2 = 1, prev1 = 1;
        for (int i = 2; i <= n; ++i) {
            int cur = 0;
            // Single-digit decode.
            if (s[i - 1] != '0') cur += prev1;
            // Two-digit decode in [10, 26].
            int two = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
            if (two >= 10 && two <= 26) cur += prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
};
