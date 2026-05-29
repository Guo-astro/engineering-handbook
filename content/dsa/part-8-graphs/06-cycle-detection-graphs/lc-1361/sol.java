// LC 1361. Validate Binary Tree Nodes
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] inDegree = new int[n];
        for (int c : leftChild) if (c != -1) inDegree[c]++;
        for (int c : rightChild) if (c != -1) inDegree[c]++;

        int root = -1;
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                if (root != -1) return false;
                root = i;
            } else if (inDegree[i] > 1) {
                return false;
            }
        }
        if (root == -1) return false;

        boolean[] seen = new boolean[n];
        seen[root] = true;
        int visitedCount = 1;
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int u = q.poll();
            int[] kids = { leftChild[u], rightChild[u] };
            for (int v : kids) {
                if (v == -1) continue;
                if (seen[v]) return false;          // cycle witness
                seen[v] = true;
                visitedCount++;
                q.offer(v);
            }
        }
        return visitedCount == n;
    }
}
