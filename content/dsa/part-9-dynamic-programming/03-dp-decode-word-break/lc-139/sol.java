// LC 139. Word Break

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Sol {
    /** LC 139 Word Break. Bottom-up O(n * L_max). */
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        Set<String> words = new HashSet<>(wordDict);
        int maxW = 0;
        for (String w : words) maxW = Math.max(maxW, w.length());
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            int lo = Math.max(0, i - maxW);
            for (int j = lo; j < i; j++) {
                if (dp[j] && words.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
