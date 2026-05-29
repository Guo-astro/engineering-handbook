// Chapter 7.0 — Recursion patterns: linear, tree, and divide-and-conquer
import java.util.HashMap;
import java.util.Map;

public final class Sol {
    private Sol() {}

    // Shape 1: linear recursion. HotSpot does NOT eliminate self-tail calls,
    // so this uses Theta(n) stack despite the tail-recursive form.
    public static long fibLinear(int n) { return fibLinearAcc(n, 0L, 1L); }

    private static long fibLinearAcc(int n, long a, long b) {
        if (n == 0) return a;
        return fibLinearAcc(n - 1, b, a + b);
    }

    // Shape 2: tree recursion. T(n) = T(n-1) + T(n-2) + O(1); exponential.
    public static long fibTree(int n) {
        if (n < 2) return n;
        return fibTree(n - 1) + fibTree(n - 2);
    }

    // Shape 2 + memo. Total Theta(n) via cached subproblems.
    public static long fibMemo(int n) {
        Map<Integer, Long> cache = new HashMap<>();
        return fibMemoHelper(n, cache);
    }

    private static long fibMemoHelper(int n, Map<Integer, Long> cache) {
        if (n < 2) return n;
        Long v = cache.get(n);
        if (v != null) return v;
        long ans = fibMemoHelper(n - 1, cache) + fibMemoHelper(n - 2, cache);
        cache.put(n, ans);
        return ans;
    }

    // Canonical entrypoint.
    public static long fib(int n) { return fibMemo(n); }

    // Shape 3: divide-and-conquer. T(n) = 2T(n/2) + Theta(n) -> Theta(n log n).
    public static int[] mergeSort(int[] nums) {
        if (nums.length <= 1) return nums.clone();
        int mid = nums.length / 2;
        int[] left = new int[mid];
        int[] right = new int[nums.length - mid];
        System.arraycopy(nums, 0, left, 0, mid);
        System.arraycopy(nums, mid, right, 0, nums.length - mid);
        return merge(mergeSort(left), mergeSort(right));
    }

    private static int[] merge(int[] a, int[] b) {
        int[] out = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) out[k++] = a[i++];
            else              out[k++] = b[j++];
        }
        while (i < a.length) out[k++] = a[i++];
        while (j < b.length) out[k++] = b[j++];
        return out;
    }
}
