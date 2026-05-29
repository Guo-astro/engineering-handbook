// LC 55. Jump Game
// five canonical cases under SolTest.
// Greedy max-reach frontier sweep. O(n) time, O(1) space.
class Sol {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
            if (maxReach >= n - 1) return true;
        }
        return true;
    }
}
