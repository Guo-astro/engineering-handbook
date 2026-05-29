// Suffix array via prefix doubling, plus Kasai LCP. O(n log^2 n) build, O(n) LCP.
import java.util.*;

public class Sol {
    public static int[] buildSuffixArray(String s) {
        int n = s.length();
        if (n == 0) return new int[0];
        Integer[] sa = new Integer[n];
        for (int i = 0; i < n; i++) sa[i] = i;
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) rank[i] = s.charAt(i);
        int[] tmp = new int[n];
        int k = 1;
        while (true) {
            final int kk = k;
            // Clone rank so the comparator reads a stable snapshot during sort.
            // Mutating the captured `rank` mid-sort would break the transitivity
            // contract and produce a non-deterministic ordering.
            final int[] r = rank.clone();
            Arrays.sort(sa, (a, b) -> {
                if (r[a] != r[b]) return Integer.compare(r[a], r[b]);
                int ra = a + kk < n ? r[a + kk] : -1;
                int rb = b + kk < n ? r[b + kk] : -1;
                return Integer.compare(ra, rb);
            });
            tmp[sa[0]] = 0;
            for (int j = 1; j < n; j++) {
                int prev = sa[j - 1], cur = sa[j];
                boolean same = r[prev] == r[cur]
                    && (prev + kk < n ? r[prev + kk] : -1)
                       == (cur + kk < n ? r[cur + kk] : -1);
                tmp[cur] = tmp[prev] + (same ? 0 : 1);
            }
            System.arraycopy(tmp, 0, rank, 0, n);
            if (rank[sa[n - 1]] == n - 1) break;
            k *= 2;
        }
        int[] out = new int[n];
        for (int i = 0; i < n; i++) out[i] = sa[i];
        return out;
    }

    public static int[] buildLcpKasai(String s, int[] sa) {
        int n = s.length();
        if (n == 0) return new int[0];
        int[] inv = new int[n];
        for (int i = 0; i < n; i++) inv[sa[i]] = i;
        int[] lcp = new int[n];
        int h = 0;
        for (int i = 0; i < n; i++) {
            if (inv[i] > 0) {
                int j = sa[inv[i] - 1];
                while (i + h < n && j + h < n && s.charAt(i + h) == s.charAt(j + h)) h++;
                lcp[inv[i]] = h;
                if (h > 0) h--;
            } else {
                h = 0;
            }
        }
        return lcp;
    }
}
