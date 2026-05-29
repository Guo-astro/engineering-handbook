// LC 384. Shuffle an Array
#include <vector>
#include <random>
#include <cstddef>

class Solution {
public:
    Solution(const std::vector<int>& nums)
        : original(nums), rng(std::random_device{}()) {}

    std::vector<int> reset() const { return original; }

    std::vector<int> shuffle() {
        std::vector<int> arr(original);
        // Durstenfeld: i descends from arr.size-1 down to 1. The
        // uniform_int_distribution<>(0, i) is inclusive on both ends, which
        // is required for uniformity. std::shuffle ships with the same loop.
        for (std::size_t i = arr.size() - 1; i > 0; --i) {
            std::uniform_int_distribution<std::size_t> dist(0, i);
            std::size_t j = dist(rng);
            std::swap(arr[i], arr[j]);
        }
        return arr;
    }

private:
    std::vector<int> original;
    std::mt19937 rng;
};
