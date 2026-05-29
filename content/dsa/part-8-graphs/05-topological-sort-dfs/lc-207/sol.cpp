// LC 207. Course Schedule
#include <vector>

class Solution {
public:
    enum Color { WHITE = 0, GRAY = 1, BLACK = 2 };

    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> adj(numCourses);
        for (const auto& e : prerequisites) {
            int a = e[0], b = e[1]; // b -> a
            adj[b].push_back(a);
        }
        std::vector<int> color(numCourses, WHITE);
        for (int u = 0; u < numCourses; ++u) {
            if (color[u] == WHITE && !dfs(u, adj, color)) return false;
        }
        return true;
    }

private:
    bool dfs(int u, const std::vector<std::vector<int>>& adj, std::vector<int>& color) {
        color[u] = GRAY;
        for (int v : adj[u]) {
            if (color[v] == GRAY) return false;        // back edge
            if (color[v] == WHITE && !dfs(v, adj, color)) return false;
        }
        color[u] = BLACK;
        return true;
    }
};
