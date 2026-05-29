// LC 128. Longest Consecutive Sequence
// Build a hash set, then for each value, only start an inner walk when
// (x - 1) is absent — i.e., x is the minimum of its run. Each element is
// touched at most twice, giving O(n) total work assuming O(1) average
// set membership. O(n) time, O(n) space.
import java.util.HashSet;
import java.util.Set;

public final class Sol {

    public static int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int x : nums) {
            s.add(x);
        }
        int best = 0;
        for (int x : s) {
            if (!s.contains(x - 1)) {
                int y = x + 1;
                while (s.contains(y)) {
                    y++;
                }
                best = Math.max(best, y - x);
            }
        }
        return best;
    }

    private Sol() {}
}
