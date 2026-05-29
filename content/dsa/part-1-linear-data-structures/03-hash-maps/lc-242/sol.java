// LC 242. Valid Anagram
// Increment-decrement-and-check: build a counter from s, then walk t
// decrementing; any underflow means t is not a permutation of s.
// Length short-circuit avoids building the counter when sizes differ.
//
// HashMap<Character, Integer> autoboxes in a tight loop; an int[26] array
// is 3-5x faster on the lowercase-ASCII case but the map version handles
// the general case unchanged.
// O(n), O(k) where k is the alphabet size.
import java.util.HashMap;
import java.util.Map;

public final class Sol {

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> counts = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            counts.merge(s.charAt(i), 1, Integer::sum);
        }
        for (int i = 0; i < t.length(); i++) {
            char ch = t.charAt(i);
            Integer c = counts.get(ch);
            if (c == null || c == 0) {
                return false;
            }
            counts.put(ch, c - 1);
        }
        return true;
    }

    private Sol() {}
}
