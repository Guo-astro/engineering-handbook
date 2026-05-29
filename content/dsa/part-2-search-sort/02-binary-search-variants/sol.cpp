// LC 33, LC 153, LC 162 plus lower_bound / upper_bound on sorted arrays
// with duplicates, plus binary search on the answer (parametric search).
//
#include <cstddef>
#include <functional>
#include <vector>

namespace dsa22 {

// Smallest index i with nums[i] >= target, or nums.size if none.
inline int lower_bound_idx(const std::vector<int>& nums, int target) {
    int lo = 0;
    int hi = static_cast<int>(nums.size());          // half-open [lo, hi)
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

// Smallest index i with nums[i] > target, or nums.size if none.
inline int upper_bound_idx(const std::vector<int>& nums, int target) {
    int lo = 0;
    int hi = static_cast<int>(nums.size());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] <= target) {                   // <= flips equality
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

// LC 33. Exact match in a rotated sorted array (distinct values).
inline int search_rotated(const std::vector<int>& nums, int target) {
    int lo = 0;
    int hi = static_cast<int>(nums.size()) - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;            // overflow-safe
        if (nums[mid] == target) return mid;
        if (nums[lo] <= nums[mid]) {
            // left half [lo..mid] is sorted
            if (nums[lo] <= target && target < nums[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        } else {
            // right half [mid..hi] is sorted
            if (nums[mid] < target && target <= nums[hi]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }
    return -1;
}

// LC 153. Minimum in a rotated sorted array of unique elements.
inline int find_min_rotated(const std::vector<int>& nums) {
    int lo = 0;
    int hi = static_cast<int>(nums.size()) - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] > nums[hi]) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return nums[lo];
}

// LC 162. Index of any strict peak (boundary sentinels -infinity).
inline int find_peak_element(const std::vector<int>& nums) {
    int lo = 0;
    int hi = static_cast<int>(nums.size()) - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] > nums[mid + 1]) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}

// Binary search on the answer (forward-ref to Part 9 / parametric search).
inline int bs_on_answer_min(int lo, int hi,
                            const std::function<bool(int)>& feasible) {
    int l = lo, r = hi;
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (feasible(mid)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return feasible(l) ? l : hi + 1;
}

} // namespace dsa22
