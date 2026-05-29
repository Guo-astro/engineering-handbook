// LC 26. Remove Duplicates from Sorted Array
public final class Sol {

    /**
     * LC 26: Remove duplicates from a sorted array in-place; return new length k.
     * Invariant: nums[0..write) is a sorted prefix of distinct elements.
     */
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int write = 1;
        for (int read = 1; read < nums.length; read++) {
            if (nums[read] != nums[write - 1]) {
                nums[write] = nums[read];
                write++;
            }
        }
        return write;
    }

    private Sol() {}
}
