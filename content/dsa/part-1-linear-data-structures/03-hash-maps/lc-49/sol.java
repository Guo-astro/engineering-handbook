// LC 49. Group Anagrams
// Bucket by canonical form. The 26-int character-count signature is O(k)
// per string vs O(k log k) for sorted-string keys. The '#' delimiter
// prevents counts like {1, 11} from colliding with {11, 1}.
// O(N * k) time, O(N * k) space, for N strings of average length k.
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class Sol {

    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String s : strs) {
            int[] counts = new int[26];
            for (int i = 0; i < s.length(); i++) {
                counts[s.charAt(i) - 'a']++;
            }
            StringBuilder key = new StringBuilder(64);
            for (int c : counts) {
                key.append('#').append(c);
            }
            groups.computeIfAbsent(key.toString(), k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }

    private Sol() {}
}
