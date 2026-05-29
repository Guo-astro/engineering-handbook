// LC 1557. Minimum Number of Vertices to Reach All Nodes
// In a DAG, a vertex is unreachable from any other vertex iff its in-degree
// is zero. The answer is the set of in-degree-zero vertices. No adjacency
// list is needed; an int[] of size n is sufficient. O(V + E) time, O(V) space.
import java.util.ArrayList;
import java.util.List;

public final class Sol {

    public static List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        int[] inDegree = new int[n];
        for (List<Integer> e : edges) {
            inDegree[e.get(1)]++;               // only the destination matters
        }
        List<Integer> out = new ArrayList<>();
        for (int u = 0; u < n; u++) {
            if (inDegree[u] == 0) {
                out.add(u);
            }
        }
        return out;
    }
}
