// LC 912. Sort an Array — heap-sort reference (in-place, O(n log n) worst case)
#include <vector>
#include <utility>

namespace heapsort_25 {

inline void siftDown(std::vector<int>& a, int root, int end) {
    while (true) {
        int left = 2 * root + 1;
        if (left >= end) return;
        int right = left + 1;
        int child = left;
        if (right < end && a[right] > a[left]) {
            child = right;
        }
        if (a[root] >= a[child]) return;
        std::swap(a[root], a[child]);
        root = child;
    }
}

inline std::vector<int> heapSort(std::vector<int> nums) {
    int n = static_cast<int>(nums.size());
    for (int start = n / 2 - 1; start >= 0; --start) {
        siftDown(nums, start, n);
    }
    for (int end = n - 1; end > 0; --end) {
        std::swap(nums[0], nums[end]);
        siftDown(nums, 0, end);
    }
    return nums;
}

}  // namespace heapsort_25
