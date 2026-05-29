// LC 847. Shortest Path Visiting All Nodes
// Bitmask BFS over (node, mask) states. n <= 12; state space n * 2^n.
// O(n^2 * 2^n) time, O(n * 2^n) space.
#include <vector>
#include <queue>
#include <tuple>

class Sol {
public:
    int shortestPathLength(std::vector<std::vector<int>>& graph) {
        int n = (int)graph.size();
        if (n == 1) return 0;
        int fullMask = (1 << n) - 1;

        std::vector<std::vector<bool>> visited(n, std::vector<bool>(1 << n, false));
        std::queue<std::tuple<int, int, int>> q;
        for (int i = 0; i < n; ++i) {
            int startMask = 1 << i;
            visited[i][startMask] = true;
            q.push({i, startMask, 0});
        }

        while (!q.empty()) {
            auto [node, mask, dist] = q.front();
            q.pop();
            if (mask == fullMask) return dist;
            for (int nb : graph[node]) {
                int newMask = mask | (1 << nb);
                if (!visited[nb][newMask]) {
                    visited[nb][newMask] = true;
                    q.push({nb, newMask, dist + 1});
                }
            }
        }

        return -1; // LC constraints guarantee connectivity; defensive.
    }
};
