// LC 136. Single Number

public final class Sol {

    /** Pair-cancel reduction. O(n) time, O(1) space. */
    public static int singleNumber(int[] nums) {
        int result = 0;
        for (int x : nums) {
            result ^= x;
        }
        return result;
    }

    private Sol() {}
}
