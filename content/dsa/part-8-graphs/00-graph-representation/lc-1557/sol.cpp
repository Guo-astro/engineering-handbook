// LC 1557. Minimum Number of Vertices to Reach All Nodes
// In a DAG, a vertex is unreachable from any other vertex iff its in-degree
// is zero. The answer is the set of in-degree-zero vertices. No adjacency
// list is needed; a single std::vector<int> of size n is sufficient.
// O(V + E) time, O(V) space.
#include <vector>

std::vector<int> findSmallestSetOfVertices(int n,
                                            const std::vector<std::vector<int>>& edges) {
    std::vector<int> inDegree(n, 0);
    for (const auto& e : edges) {
        inDegree[e[1]]++;                       // only the destination matters
    }
    std::vector<int> out;
    for (int u = 0; u < n; ++u) {
        if (inDegree[u] == 0) {
            out.push_back(u);
        }
    }
    return out;
}
