// LC 5. Longest Palindromic Substring
public final class Sol {

    /** LC 5. Return any longest palindromic substring of s. */
    public static String longestPalindrome(String s) {
        if (s.isEmpty()) return "";
        int bestL = 0, bestR = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] odd = expand(s, i, i);
            int[] even = expand(s, i, i + 1);
            if (odd[1] - odd[0] > bestR - bestL) {
                bestL = odd[0];
                bestR = odd[1];
            }
            if (even[1] - even[0] > bestR - bestL) {
                bestL = even[0];
                bestR = even[1];
            }
        }
        return s.substring(bestL, bestR + 1);
    }

    private static int[] expand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return new int[] { left + 1, right - 1 };
    }

    private Sol() {}
}
