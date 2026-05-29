// LC 215. Kth Largest Element in an Array
import java.util.concurrent.ThreadLocalRandom;

public class Sol {
    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k;
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int pivotIdx = partition(nums, lo, hi);
            if (pivotIdx == target) {
                return nums[pivotIdx];
            }
            if (pivotIdx < target) {
                lo = pivotIdx + 1;
            } else {
                hi = pivotIdx - 1;
            }
        }
        return -1;  // unreachable for valid input
    }

    private int partition(int[] nums, int lo, int hi) {
        int randIdx = ThreadLocalRandom.current().nextInt(lo, hi + 1);
        swap(nums, randIdx, hi);
        int pivot = nums[hi];
        int store = lo;
        for (int i = lo; i < hi; i++) {
            if (nums[i] < pivot) {
                swap(nums, store, i);
                store++;
            }
        }
        swap(nums, store, hi);
        return store;
    }

    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a]; nums[a] = nums[b]; nums[b] = tmp;
    }
}
