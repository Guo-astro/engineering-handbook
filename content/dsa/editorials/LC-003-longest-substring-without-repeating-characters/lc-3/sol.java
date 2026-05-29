// LC 3. Longest Substring Without Repeating Characters
import java.util.HashMap;
import java.util.Map;

public final class Sol {

    /** LC 3. Length of the longest substring with no repeating characters. */
    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastIndex = new HashMap<>();
        int l = 0;
        int best = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            Integer prev = lastIndex.get(c);
            if (prev != null && prev >= l) {
                l = prev + 1;
            }
            lastIndex.put(c, r);
            if (r - l + 1 > best) {
                best = r - l + 1;
            }
        }
        return best;
    }

    private Sol() {}
}
