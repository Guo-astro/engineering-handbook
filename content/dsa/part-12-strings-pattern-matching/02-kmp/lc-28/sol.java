// LC 28. Find the Index of the First Occurrence in a String
public final class Sol {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0;
        int n = haystack.length();
        int m = needle.length();
        if (m > n) return -1;
        int[] lps = computeLps(needle);
        int i = 0, j = 0;
        while (i < n) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
                if (j == m) return i - j;
            } else {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
        return -1;
    }

    public int[] computeLps(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int length = 0;
        int i = 1;
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) length = lps[length - 1];
                else { lps[i] = 0; i++; }
            }
        }
        return lps;
    }
}
