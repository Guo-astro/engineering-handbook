// LC 3. Longest Substring Without Repeating Characters
import java.util.HashMap;
import java.util.Map;

public final class Sol {

    /**
     * LC 3 (last-index-jump form). For each new character, if it has been
     * seen before AND that prior index lies inside the current window
     * (last >= l), jump l to last + 1 in O(1). The `last >= l` guard keeps
     * stale entries from outside the window from triggering a wrong jump.
     */
    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> last = new HashMap<>();
        int l = 0;
        int best = 0;
        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);
            Integer prev = last.get(ch);
            if (prev != null && prev >= l) {
                l = prev + 1;
            }
            last.put(ch, r);
            if (r - l + 1 > best) {
                best = r - l + 1;
            }
        }
        return best;
    }

    private Sol() {}
}
