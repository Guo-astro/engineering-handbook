// LC 1042. Flower Planting With No Adjacent
// NOT a 2-coloring: 4 flower types over a max-degree-3 graph (greedy works).
import java.util.*;

public class Sol {
    public static int[] gardenNoAdj(int n, int[][] paths) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>()); // 1-indexed
        for (int[] p : paths) {
            graph.get(p[0]).add(p[1]);
            graph.get(p[1]).add(p[0]);
        }

        int[] answer = new int[n + 1];                    // 0 = unassigned; flowers 1..4
        for (int u = 1; u <= n; u++) {
            boolean[] used = new boolean[5];              // index 1..4
            for (int v : graph.get(u)) {
                if (answer[v] != 0) used[answer[v]] = true;
            }
            for (int flower = 1; flower <= 4; flower++) {
                if (!used[flower]) {
                    answer[u] = flower;
                    break;
                }
            }
        }
        int[] result = new int[n];
        System.arraycopy(answer, 1, result, 0, n);
        return result;
    }
}
