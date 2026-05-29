// LC 560. Subarray Sum Equals K
import java.util.HashMap;

public final class Sol {

    // LC 560.
    public static int subarraySum(int[] nums, int k) {
        HashMap<Long, Integer> counts = new HashMap<>();
        counts.put(0L, 1);
        long prefix = 0;
        int answer = 0;
        long kL = (long) k;
        for (int x : nums) {
            prefix += x;
            // getOrDefault avoids a get-then-null-check; merge avoids a
            // get-then-put double lookup on the increment.
            answer += counts.getOrDefault(prefix - kL, 0);
            counts.merge(prefix, 1, Integer::sum);
        }
        return answer;
    }

    private Sol() {}
}
