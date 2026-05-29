// LC 239. Sliding Window Maximum
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] out = new int[n - k + 1];
        // Deque of indices; nums[deque[front..back]] is strictly decreasing.
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            // Drop the front if it has fallen out of the window.
            if (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }
            // Maintain monotone-decreasing back.
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {
                dq.pollLast();
            }
            dq.offerLast(i);
            if (i >= k - 1) {
                out[i - k + 1] = nums[dq.peekFirst()];
            }
        }
        return out;
    }
}
