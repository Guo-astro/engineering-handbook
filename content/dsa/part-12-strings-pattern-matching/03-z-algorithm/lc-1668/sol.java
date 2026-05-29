// LC 1668. Maximum Repeating Substring
import java.util.Arrays;

public class Sol {
    /** Z-array of s in O(n). z[0] = 0 by convention. */
    public static int[] zFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i < r) {
                z[i] = Math.min(r - i, z[i - l]);
            }
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }
        return z;
    }

    /** LC 1668: largest k such that word^k occurs as a substring of sequence. */
    public static int maxRepeating(String sequence, String word) {
        int m = word.length();
        int n = sequence.length();
        if (m == 0 || m > n) return 0;
        String s = word + "#" + sequence;
        int[] z = zFunction(s);
        int best = 0;
        for (int start = 0; start < n; start++) {
            int i = m + 1 + start;
            int run = 0;
            while (i + m <= s.length() && z[i] >= m) {
                run++;
                i += m;
            }
            if (run > best) best = run;
        }
        return best;
    }
}
