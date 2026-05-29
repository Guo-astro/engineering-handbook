// LC 189. Rotate Array
// Three-reverse trick: reverse the whole array, then reverse the first k,
// then reverse the rest. Avoids the O(n*k) naive shift. O(n), O(1).
public final class Sol {

    public static void rotate(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) return;
        k %= n; // Tolerate k > n; rotating n is a no-op.
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private static void reverse(int[] a, int lo, int hi) {
        while (lo < hi) {
            int t = a[lo];
            a[lo] = a[hi];
            a[hi] = t;
            lo++;
            hi--;
        }
    }

    private Sol() {}
}
