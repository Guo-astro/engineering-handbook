// LC 303. Range Sum Query - Immutable
public final class Sol {

    /** LC 303. Construct in O(n); sumRange in O(1). */
    public static class NumArray {
        private final long[] prefix;

        public NumArray(int[] nums) {
            int n = nums.length;
            // prefix[0] = 0 is the empty-sum sentinel.
            this.prefix = new long[n + 1];
            for (int i = 0; i < n; i++) {
                this.prefix[i + 1] = this.prefix[i] + nums[i];
            }
        }

        public int sumRange(int left, int right) {
            return (int) (this.prefix[right + 1] - this.prefix[left]);
        }
    }

    private Sol() {}
}
