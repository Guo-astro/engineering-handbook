// LC 704. Binary Search. Exact-match closed-interval template.
// LC 35. Search Insert Position. Lower-bound half-open template.
// LC 278. First Bad Version. Predicate-driven half-open template.

#include <functional>
#include <vector>

class Solution {
public:
    // LC 704. Exact-match closed-interval template.
    int search(const std::vector<int>& nums, int target) {
        int lo = 0;
        int hi = static_cast<int>(nums.size()) - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;  // overflow-safe vs (lo + hi) / 2
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return -1;
    }

    // LC 35. Lower-bound; same shape as std::lower_bound on a std::vector<int>.
    int searchInsert(const std::vector<int>& nums, int target) {
        int lo = 0;
        int hi = static_cast<int>(nums.size());
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

    // LC 278. Predicate-driven leftmost template on [1, n].
    int firstBadVersion(int n, const std::function<bool(int)>& isBadVersion) {
        int lo = 1, hi = n;
        while (lo < hi) {
            // overflow-safe; lo + hi can overflow signed int near INT_MAX
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
