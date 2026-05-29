// LC 274. H-Index (counting sort with cap-at-n)
#include <algorithm>
#include <vector>

// Stable counting sort over bounded integer keys.
// Time: O(n + k) where k = max - min + 1.
// Space: O(n + k).
// Stability comes from the back-to-front scatter with decrement-before-write.
std::vector<int> countingSort(const std::vector<int>& nums) {
    if (nums.empty()) return {};
    const auto [lo_it, hi_it] = std::minmax_element(nums.begin(), nums.end());
    const int lo = *lo_it;
    const int hi = *hi_it;
    const int k = hi - lo + 1;
    std::vector<int> count(k, 0);
    for (int x : nums) ++count[x - lo];
    for (int i = 1; i < k; ++i) count[i] += count[i - 1];
    std::vector<int> out(nums.size());
    for (int i = static_cast<int>(nums.size()) - 1; i >= 0; --i) {
        const int x = nums[i];
        --count[x - lo];
        out[count[x - lo]] = x;
    }
    return out;
}

// LC 274 H-Index via counting sort with the cap-at-n trick.
// The answer cannot exceed n, so capping each citation at n collapses
// the universe to [0, n]; counting sort runs in O(n) time and space.
int hIndex(const std::vector<int>& citations) {
    const int n = static_cast<int>(citations.size());
    std::vector<int> count(n + 1, 0);
    for (int c : citations) ++count[std::min(c, n)];
    int total = 0;
    for (int h = n; h >= 0; --h) {
        total += count[h];
        if (total >= h) return h;
    }
    return 0;
}
