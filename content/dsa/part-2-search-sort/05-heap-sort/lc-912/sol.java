// LC 912. Sort an Array — heap-sort reference (in-place, O(n log n) worst case)
public class Sol {

    public static int[] heapSort(int[] nums) {
        int n = nums.length;
        // Phase 1: Floyd's build-max-heap, right-to-left.
        for (int start = n / 2 - 1; start >= 0; start--) {
            siftDown(nums, start, n);
        }
        // Phase 2: extract max into the sorted suffix.
        for (int end = n - 1; end > 0; end--) {
            int tmp = nums[0];
            nums[0] = nums[end];
            nums[end] = tmp;
            siftDown(nums, 0, end);
        }
        return nums;
    }

    private static void siftDown(int[] a, int root, int end) {
        while (true) {
            int left = 2 * root + 1;
            if (left >= end) return;
            int right = left + 1;
            int child = left;
            if (right < end && a[right] > a[left]) {
                child = right;
            }
            if (a[root] >= a[child]) return;
            int tmp = a[root]; a[root] = a[child]; a[child] = tmp;
            root = child;
        }
    }
}
