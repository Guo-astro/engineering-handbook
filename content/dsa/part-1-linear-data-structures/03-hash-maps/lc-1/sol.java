// LC 1. Two Sum
// One pass with a value -> first-seen-index map. Look up the complement
// BEFORE inserting; the lookup-then-insert order prevents matching an
// element against itself on inputs like [3, 3]. O(n) time, O(n) space.
import java.util.HashMap;
import java.util.Map;

public final class Sol {

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }

    private Sol() {}
}
