// LC 1584. Min Cost to Connect All Points
#include <vector>
#include <queue>
#include <utility>
#include <cstdlib>

class Solution {
public:
    int minCostConnectPoints(std::vector<std::vector<int>>& points) {
        int n = (int)points.size();
        if (n <= 1) return 0;
        std::vector<bool> in_mst(n, false);
        using P = std::pair<int,int>;       // (weight, vertex)
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.emplace(0, 0);
        int total = 0;
        int edges_added = 0;
        while (!pq.empty() && edges_added < n) {
            auto [w, u] = pq.top();
            pq.pop();
            if (in_mst[u]) continue;        // stale entry
            in_mst[u] = true;
            total += w;
            ++edges_added;
            for (int v = 0; v < n; ++v) {
                if (!in_mst[v]) {
                    int d = std::abs(points[u][0] - points[v][0])
                          + std::abs(points[u][1] - points[v][1]);
                    pq.emplace(d, v);
                }
            }
        }
        return total;
    }
};
