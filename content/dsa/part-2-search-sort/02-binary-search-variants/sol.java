// LC 33, LC 153, LC 162 plus lower_bound / upper_bound on sorted arrays
// with duplicates, plus binary search on the answer (parametric search).
//
// The closed-interval (Template A) and half-open (Templates B/C) invariants
// from chapter 2.1 carry through. The change per variant is the comparison
// driving the halving.
//
import java.util.function.IntPredicate;

public class Sol {

    // Smallest index i with nums[i] >= target, or nums.length if none.
    public static int lowerBound(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length;                       // half-open [lo, hi)
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

    // Smallest index i with nums[i] > target, or nums.length if none.
    public static int upperBound(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] <= target) {              // <= flips equality
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    // LC 33. Exact match in a rotated sorted array (distinct values).
    public static int searchRotated(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;            // overflow-safe midpoint
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
    public static int findMinRotated(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;
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
    public static int findPeakElement(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;
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
    // Returns smallest X in [lo, hi] with feasible(X) true; hi + 1 if none.
    public static int bsOnAnswerMin(int lo, int hi, IntPredicate feasible) {
        int l = lo, r = hi;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (feasible.test(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return feasible.test(l) ? l : hi + 1;
    }
}
