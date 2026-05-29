// LC 213. House Robber II
public class Sol {
    /** LC 213 House Robber II. Circular reduces to two linear sub-ranges. */
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        return Math.max(robLinear(nums, 0, n - 2),
                        robLinear(nums, 1, n - 1));
    }

    /** Linear House Robber on nums[lo..hi] inclusive. Rolling pair, O(1) space. */
    private int robLinear(int[] nums, int lo, int hi) {
        int prev2 = 0, prev1 = 0;
        for (int i = lo; i <= hi; i++) {
            int curr = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
}
