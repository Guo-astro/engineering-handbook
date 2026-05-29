// LC 785. Is Graph Bipartite?
#include <vector>
#include <queue>

class Solution {
public:
    bool isBipartite(std::vector<std::vector<int>>& graph) {
        int n = (int)graph.size();
        std::vector<int> color(n, 0);          // 0 = unvisited, 1 / -1 = two classes
        for (int start = 0; start < n; ++start) {
            if (color[start] != 0) continue;
            color[start] = 1;
            std::queue<int> q;
            q.push(start);
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : graph[u]) {
                    if (color[v] == 0) {
                        color[v] = -color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
