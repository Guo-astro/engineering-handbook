// LC 1668. Maximum Repeating Substring
#include <algorithm>
#include <string>
#include <vector>

std::vector<int> z_function(const std::string& s) {
    int n = static_cast<int>(s.size());
    std::vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i < r) {
            z[i] = std::min(r - i, z[i - l]);
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}

int max_repeating(const std::string& sequence, const std::string& word) {
    int m = static_cast<int>(word.size());
    int n = static_cast<int>(sequence.size());
    if (m == 0 || m > n) return 0;
    std::string s = word + "#" + sequence;
    auto z = z_function(s);
    int best = 0;
    for (int start = 0; start < n; ++start) {
        int i = m + 1 + start;
        int run = 0;
        while (i + m <= static_cast<int>(s.size()) && z[i] >= m) {
            ++run;
            i += m;
        }
        if (run > best) best = run;
    }
    return best;
}
