// LC 763. Partition Labels
import java.util.ArrayList;
import java.util.List;

public final class Sol {

    public List<Integer> partitionLabels(String s) {
        // last[c]: rightmost index at which character c appears.
        // Alphabet is lowercase ASCII; int[26] is the canonical idiom.
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }
        List<Integer> parts = new ArrayList<>();
        int start = 0;
        int end = 0;
        for (int i = 0; i < s.length(); i++) {
            // Greedy step: extend the right boundary to the farthest
            // last-occurrence among characters in the current window.
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                parts.add(end - start + 1);
                start = i + 1;
            }
        }
        return parts;
    }
}
