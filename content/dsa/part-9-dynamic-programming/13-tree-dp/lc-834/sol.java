// LC 834. Sum of Distances in Tree
// implements the re-rooting technique sketched in
//  (pattern extension).
import java.util.ArrayList;
import java.util.List;

public final class Sol {

    private List<List<Integer>> adj;
    private int[] count;
    private int[] answer;
    private int n;

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        this.n = n;
        if (n == 1) return new int[]{0};
        this.adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        this.count  = new int[n];
        this.answer = new int[n];
        for (int i = 0; i < n; i++) count[i] = 1;
        // Pass 1: post-order DFS — fill count[] and answer[0].
        post(0, -1);
        // Pass 2: pre-order DFS — re-root from u to each child v in O(1).
        pre(0, -1);
        return answer;
    }

    private void post(int u, int parent) {
        for (int v : adj.get(u)) {
            if (v == parent) continue;
            post(v, u);
            count[u]  += count[v];
            answer[u] += answer[v] + count[v];
        }
    }

    private void pre(int u, int parent) {
        for (int v : adj.get(u)) {
            if (v == parent) continue;
            // Re-root: count[v] nodes get 1 closer, (n - count[v]) get 1 farther.
            answer[v] = answer[u] - count[v] + (n - count[v]);
            pre(v, u);
        }
    }
}
