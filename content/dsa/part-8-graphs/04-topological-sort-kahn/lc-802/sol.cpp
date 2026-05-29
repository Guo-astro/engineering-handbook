// LC 802. Find Eventual Safe States
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> eventualSafeNodes(std::vector<std::vector<int>>& graph) {
        int n = (int)graph.size();
        std::vector<int> revIndeg(n, 0);                  // = original out-degree
        std::vector<std::vector<int>> revAdj(n);
        for (int u = 0; u < n; ++u) {
            for (int v : graph[u]) {
                revAdj[v].push_back(u);                    // reverse edge v -> u
                revIndeg[u]++;
            }
        }
        std::queue<int> q;
        for (int v = 0; v < n; ++v) if (revIndeg[v] == 0) q.push(v);
        std::vector<bool> safe(n, false);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            safe[u] = true;
            for (int v : revAdj[u]) {
                if (--revIndeg[v] == 0) q.push(v);
            }
        }
        std::vector<int> ans;
        for (int v = 0; v < n; ++v) if (safe[v]) ans.push_back(v);
        return ans;
    }
};
