// LC 27. Remove Element
// Two-pointer compaction: read pointer i scans every slot, write pointer k
// advances only on keepers. Returns the new logical length. O(n), O(1).
public final class Sol {

    public static int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }

    private Sol() {}
}
