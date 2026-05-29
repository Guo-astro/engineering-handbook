// LC 643. Maximum Average Subarray I
public final class Sol {

    /** LC 643. Track the running window sum as long; postpone float division. */
    public static double findMaxAverage(int[] nums, int k) {
        long windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }
        long bestSum = windowSum;
        for (int r = k; r < nums.length; r++) {
            windowSum += nums[r] - nums[r - k];
            if (windowSum > bestSum) {
                bestSum = windowSum;
            }
        }
        return (double) bestSum / k;
    }

    private Sol() {}
}
