// LC 5. Longest Palindromic Substring
public class Sol {
    // Approach A: 2D DP by-length. O(n^2) time, O(n^2) space.
    public static String longestPalindrome(String s) {
        int n = s.length();
        if (n == 0) return "";
        boolean[][] isPalin = new boolean[n][n];
        int start = 0, maxLen = 1;

        // Length 1.
        for (int i = 0; i < n; i++) isPalin[i][i] = true;

        // Length 2.
        for (int i = 0; i + 1 < n; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                isPalin[i][i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }

        // Length L from 3 to n.
        for (int L = 3; L <= n; L++) {
            for (int i = 0; i + L - 1 < n; i++) {
                int j = i + L - 1;
                if (s.charAt(i) == s.charAt(j) && isPalin[i + 1][j - 1]) {
                    isPalin[i][j] = true;
                    if (L > maxLen) {
                        start = i;
                        maxLen = L;
                    }
                }
            }
        }
        return s.substring(start, start + maxLen);
    }

    // Approach B: expand around centers. O(n^2) time, O(1) space.
    public static String longestPalindromeCenters(String s) {
        if (s.isEmpty()) return "";
        int bestL = 0, bestR = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] odd = expand(s, i, i);
            int[] even = expand(s, i, i + 1);
            if (odd[1] - odd[0] > bestR - bestL) { bestL = odd[0]; bestR = odd[1]; }
            if (even[1] - even[0] > bestR - bestL) { bestL = even[0]; bestR = even[1]; }
        }
        return s.substring(bestL, bestR + 1);
    }

    private static int[] expand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return new int[]{left + 1, right - 1};
    }
}
