// Suffix array via prefix doubling, plus Kasai LCP. O(n log^2 n) build, O(n) LCP.
#include <algorithm>
#include <string>
#include <vector>

std::vector<int> build_suffix_array(const std::string& s) {
    int n = static_cast<int>(s.size());
    if (n == 0) return {};
    std::vector<int> sa(n), rank(n), tmp(n);
    for (int i = 0; i < n; ++i) {
        sa[i] = i;
        rank[i] = static_cast<unsigned char>(s[i]);
    }
    int k = 1;
    while (true) {
        auto key = [&](int i) {
            int second = (i + k < n) ? rank[i + k] : -1;
            return std::make_pair(rank[i], second);
        };
        std::sort(sa.begin(), sa.end(), [&](int a, int b) {
            return key(a) < key(b);
        });
        tmp[sa[0]] = 0;
        for (int j = 1; j < n; ++j) {
            tmp[sa[j]] = tmp[sa[j - 1]]
                       + (key(sa[j]) != key(sa[j - 1]) ? 1 : 0);
        }
        rank = tmp;
        if (rank[sa[n - 1]] == n - 1) break;
        k *= 2;
    }
    return sa;
}

std::vector<int> build_lcp_kasai(const std::string& s,
                                 const std::vector<int>& sa) {
    int n = static_cast<int>(s.size());
    if (n == 0) return {};
    std::vector<int> inv(n), lcp(n, 0);
    for (int i = 0; i < n; ++i) inv[sa[i]] = i;
    int h = 0;
    for (int i = 0; i < n; ++i) {
        if (inv[i] > 0) {
            int j = sa[inv[i] - 1];
            while (i + h < n && j + h < n && s[i + h] == s[j + h]) ++h;
            lcp[inv[i]] = h;
            if (h > 0) --h;
        } else {
            h = 0;
        }
    }
    return lcp;
}
