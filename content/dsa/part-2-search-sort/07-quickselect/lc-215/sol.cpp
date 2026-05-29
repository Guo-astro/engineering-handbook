// LC 215. Kth Largest Element in an Array
#include <random>
#include <utility>
#include <vector>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        int target = static_cast<int>(nums.size()) - k;
        int lo = 0;
        int hi = static_cast<int>(nums.size()) - 1;
        while (lo <= hi) {
            int pivot_idx = partition(nums, lo, hi);
            if (pivot_idx == target) {
                return nums[pivot_idx];
            }
            if (pivot_idx < target) {
                lo = pivot_idx + 1;
            } else {
                hi = pivot_idx - 1;
            }
        }
        return -1;  // unreachable for valid input
    }

private:
    int partition(std::vector<int>& nums, int lo, int hi) {
        static thread_local std::mt19937 rng{std::random_device{}()};
        std::uniform_int_distribution<int> dist(lo, hi);
        int rand_idx = dist(rng);
        std::swap(nums[rand_idx], nums[hi]);
        int pivot = nums[hi];
        int store = lo;
        for (int i = lo; i < hi; ++i) {
            if (nums[i] < pivot) {
                std::swap(nums[store], nums[i]);
                ++store;
            }
        }
        std::swap(nums[store], nums[hi]);
        return store;
    }
};
