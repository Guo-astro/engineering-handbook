// LC 128. Longest Consecutive Sequence
// Build a hash set, then for each value, only start an inner walk when
// (x - 1) is absent — i.e., x is the minimum of its run. Each element is
// touched at most twice, giving O(n) total work assuming O(1) average
// set membership. O(n) time, O(n) space.
#include <unordered_set>
#include <vector>
#include <algorithm>

int longestConsecutive(const std::vector<int>& nums) {
    std::unordered_set<int> s(nums.begin(), nums.end());
    int best = 0;
    for (int x : s) {
        if (s.find(x - 1) == s.end()) {
            int y = x + 1;
            while (s.find(y) != s.end()) {
                ++y;
            }
            best = std::max(best, y - x);
        }
    }
    return best;
}
