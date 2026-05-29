// LC 704. Binary Search. Exact-match closed-interval template.
// LC 35. Search Insert Position. Lower-bound half-open template.
// LC 278. First Bad Version. Predicate-driven half-open template.

public class Solution {

    /** LC 704. Exact-match closed-interval template. */
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            // overflow-safe midpoint per Bloch 2006
            int mid = lo + (hi - lo) / 2;
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

    /** LC 35. Lower-bound (leftmost insertion point), half-open [lo, hi). */
    public int searchInsert(int[] nums, int target) {
        int lo = 0, hi = nums.length;
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

    /** LC 278. Predicate-driven leftmost template on [1, n].
     *  oracle is the isBadVersion API; in production extends VersionControl. */
    public interface BadVersionOracle {
        boolean isBadVersion(int version);
    }

    public int firstBadVersion(int n, BadVersionOracle oracle) {
        int lo = 1, hi = n;
        while (lo < hi) {
            // overflow-safe; lo + hi can overflow when n approaches Integer.MAX_VALUE
            int mid = lo + (hi - lo) / 2;
            if (oracle.isBadVersion(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
