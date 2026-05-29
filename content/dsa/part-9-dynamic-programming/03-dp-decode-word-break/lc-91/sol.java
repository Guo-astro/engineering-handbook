// LC 91. Decode Ways

class Sol {
    /** LC 91 Decode Ways. Returns number of decodings of the digit string s. */
    public int numDecodings(String s) {
        int n = s.length();
        if (n == 0 || s.charAt(0) == '0') return 0;
        // Rolling window: prev2 = dp[i-2], prev1 = dp[i-1].
        int prev2 = 1, prev1 = 1;
        for (int i = 2; i <= n; i++) {
            int cur = 0;
            // Single-digit decode.
            if (s.charAt(i - 1) != '0') cur += prev1;
            // Two-digit decode in [10, 26].
            int two = Integer.parseInt(s.substring(i - 2, i));
            if (two >= 10 && two <= 26) cur += prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
