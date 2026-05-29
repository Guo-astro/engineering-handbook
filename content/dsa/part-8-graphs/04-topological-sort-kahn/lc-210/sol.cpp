// LC 210. Course Schedule II
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> findOrder(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<int> indeg(numCourses, 0);
        std::vector<std::vector<int>> adj(numCourses);
        for (const auto& e : prerequisites) {
            int a = e[0], b = e[1]; // b -> a
            adj[b].push_back(a);
            indeg[a]++;
        }
        std::queue<int> q;
        for (int v = 0; v < numCourses; ++v) if (indeg[v] == 0) q.push(v);
        std::vector<int> order;
        order.reserve(numCourses);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (--indeg[v] == 0) q.push(v);
            }
        }
        if ((int)order.size() != numCourses) return {};
        return order;
    }
};
