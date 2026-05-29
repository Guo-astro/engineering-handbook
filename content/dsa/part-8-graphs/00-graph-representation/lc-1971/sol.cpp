// LC 1971. Find if Path Exists in Graph
// reachability cases match.
// Build an adjacency list from the edges, then BFS from source. Build and
// BFS are each O(V + E); std::vector<bool> visited is the standard packed
// bit-vector idiom for membership in this size regime.
#include <queue>
#include <vector>

bool validPath(int n,
               const std::vector<std::vector<int>>& edges,
               int source,
               int destination) {
    if (source == destination) {
        return true;
    }
    std::vector<std::vector<int>> adj(n);
    for (const auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);              // undirected: push both halves
    }
    std::vector<bool> visited(n, false);
    visited[source] = true;
    std::queue<int> q;
    q.push(source);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (v == destination) {
                return true;
            }
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
    return false;
}
