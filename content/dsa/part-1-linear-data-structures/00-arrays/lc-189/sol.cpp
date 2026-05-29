// LC 189. Rotate Array
// Three-reverse trick: reverse the whole array, then reverse the first k,
// then reverse the rest. Avoids the O(n*k) naive shift. O(n), O(1).
#include <vector>
#include <algorithm>

void rotate(std::vector<int>& nums, int k) {
    int n = static_cast<int>(nums.size());
    if (n == 0) return;
    k %= n; // Tolerate k > n; rotating n is a no-op.
    std::reverse(nums.begin(), nums.end());
    std::reverse(nums.begin(), nums.begin() + k);
    std::reverse(nums.begin() + k, nums.end());
}
