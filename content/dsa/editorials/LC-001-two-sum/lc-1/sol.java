// LC 1. Two Sum
import java.util.HashMap;
import java.util.Map;

public final class Sol {

    /** LC 1. Return indices of two numbers summing to target. */
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
