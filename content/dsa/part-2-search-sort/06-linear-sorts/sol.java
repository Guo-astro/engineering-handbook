// LC 274. H-Index (counting sort with cap-at-n)
import java.util.Arrays;

public class Sol {
    /**
     * Stable counting sort over bounded integer keys.
     * Time:  O(n + k) where k = max - min + 1.
     * Space: O(n + k).
     * Stability comes from the back-to-front scatter with decrement-before-write.
     */
    public static int[] countingSort(int[] nums) {
        if (nums.length == 0) return new int[0];
        int lo = nums[0], hi = nums[0];
        for (int x : nums) {
            if (x < lo) lo = x;
            if (x > hi) hi = x;
        }
        int k = hi - lo + 1;
        int[] count = new int[k];
        for (int x : nums) count[x - lo]++;
        for (int i = 1; i < k; i++) count[i] += count[i - 1];
        int[] out = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            int x = nums[i];
            count[x - lo]--;
            out[count[x - lo]] = x;
        }
        return out;
    }

    /**
     * LC 274 H-Index via counting sort with the cap-at-n trick.
     * The answer cannot exceed n, so capping each citation at n collapses
     * the universe to [0, n]; counting sort runs in O(n) time and space.
     */
    public static int hIndex(int[] citations) {
        int n = citations.length;
        int[] count = new int[n + 1];
        for (int c : citations) count[Math.min(c, n)]++;
        int total = 0;
        for (int h = n; h >= 0; h--) {
            total += count[h];
            if (total >= h) return h;
        }
        return 0;
    }
}
