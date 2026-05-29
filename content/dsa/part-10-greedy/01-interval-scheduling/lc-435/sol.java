// LC 435. Non-overlapping Intervals
//
// Sort by END ascending; walk; drop on overlap, otherwise advance the cursor.
// Integer.compare guards against overflow on adversarial endpoint values
// (the a[1] - b[1] subtraction idiom is broken near Integer.MAX_VALUE).
import java.util.Arrays;

public class Sol {
    public static int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int removed = 0;
        int currentEnd = Integer.MIN_VALUE;
        for (int[] iv : intervals) {
            if (iv[0] < currentEnd) {
                // Overlap with the earlier-ending interval we kept; drop this one.
                removed++;
            } else {
                currentEnd = iv[1];
            }
        }
        return removed;
    }
}
