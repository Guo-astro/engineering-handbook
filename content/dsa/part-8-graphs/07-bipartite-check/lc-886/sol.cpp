// LC 886. Possible Bipartition
// Build adjacency from 1-indexed dislikes, then run standard 2-coloring BFS.
#include <vector>
#include <queue>

class Solution {
public:
    bool possibleBipartition(int n, std::vector<std::vector<int>>& dislikes) {
        std::vector<std::vector<int>> graph(n + 1);   // 1-indexed; slot 0 unused
        for (auto& d : dislikes) {
            graph[d[0]].push_back(d[1]);
            graph[d[1]].push_back(d[0]);
        }

        std::vector<int> color(n + 1, 0);             // 0 = unvisited, 1 / -1 = two groups
        for (int start = 1; start <= n; ++start) {
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
