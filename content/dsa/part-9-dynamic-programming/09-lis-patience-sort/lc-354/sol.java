// LC 354. Russian Doll Envelopes
import java.util.Arrays;

public class Sol {
    public static int lengthOfLis(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            // lower_bound on tails[0..size): leftmost index where tails[i] >= x.
            int lo = 0, hi = size;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;          // unsigned-shift midpoint avoids overflow
                if (tails[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            tails[lo] = x;
            if (lo == size) size++;
        }
        return size;
    }

    public static int maxEnvelopes(int[][] envelopes) {
        if (envelopes.length == 0) return 0;
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]);     // height DESC on width tie
        });
        int[] heights = new int[envelopes.length];
        for (int i = 0; i < envelopes.length; i++) heights[i] = envelopes[i][1];
        return lengthOfLis(heights);
    }
}
