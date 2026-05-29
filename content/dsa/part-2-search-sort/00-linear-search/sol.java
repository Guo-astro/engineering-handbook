// LC linear search — Knuth Algorithm B (The Art of Computer Programming Vol 3 §6.1).
// Primitive int[] (not Integer[]) per the four-language idiom contract: avoids
// boxing on the hot path. Returns the first index where nums[i] == target,
// or -1 if no such index exists.
public class Sol {

    /**
     * Linear scan over an unsorted int array.
     * <p>
     * Loop invariant: at the start of each iteration of the for loop,
     * nums[0..i-1] does not contain target.
     * <ul>
     *     <li>Initialisation (i = 0): the empty prefix vacuously contains nothing.</li>
     *     <li>Maintenance: either nums[i] == target and we return i, or nums[i] != target
     *         and the invariant extends to nums[0..i].</li>
     *     <li>Termination (i = nums.length): no index matched, return -1.</li>
     * </ul>
     */
    public static int linearSearch(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
