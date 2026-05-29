// LC 28. Find the Index of the First Occurrence in a String
public final class Sol {

    /** LC 28. Rabin-Karp first-occurrence search; expected O(n + m). */
    public static int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) return 0;
        if (m > n)  return -1;

        // long products: (mod - 1) * base fits comfortably in 2^63 - 1.
        // Casting to long is the canonical guard against signed-overflow UB.
        final long base = 256L;
        final long mod  = 1_000_000_007L;

        long highPower = 1L;
        for (int i = 0; i < m - 1; i++) {
            highPower = (highPower * base) % mod;
        }

        long needleHash = 0L, windowHash = 0L;
        for (int i = 0; i < m; i++) {
            needleHash = (needleHash * base + needle.charAt(i)) % mod;
            windowHash = (windowHash * base + haystack.charAt(i)) % mod;
        }

        for (int i = 0; i <= n - m; i++) {
            if (windowHash == needleHash
                    && haystack.regionMatches(i, needle, 0, m)) {
                return i;
            }
            if (i < n - m) {
                long leading = (haystack.charAt(i) * highPower) % mod;
                // + mod before subtract: keeps the result non-negative.
                windowHash = (windowHash - leading + mod) % mod;
                windowHash = (windowHash * base + haystack.charAt(i + m)) % mod;
            }
        }
        return -1;
    }

    private Sol() {}
}
