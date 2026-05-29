// LC 1584. Min Cost to Connect All Points
#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> parent;
    std::vector<int> rank_;

    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];   // path halving
            x = parent[x];
        }
        return x;
    }

    bool unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (rank_[ra] < rank_[rb]) std::swap(ra, rb);
        parent[rb] = ra;
        if (rank_[ra] == rank_[rb]) rank_[ra]++;
        return true;
    }

    int minCostConnectPoints(std::vector<std::vector<int>>& points) {
        int n = static_cast<int>(points.size());
        if (n <= 1) return 0;
        std::vector<std::tuple<int, int, int>> edges; // (w, u, v)
        edges.reserve(static_cast<std::size_t>(n) * (n - 1) / 2);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int w = std::abs(points[i][0] - points[j][0])
                      + std::abs(points[i][1] - points[j][1]);
                edges.emplace_back(w, i, j);
            }
        }
        std::sort(edges.begin(), edges.end());
        parent.assign(n, 0);
        rank_.assign(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
        long long total = 0;        // long long: sum can exceed INT_MAX
        int accepted = 0;
        for (auto& [w, u, v] : edges) {
            if (unite(u, v)) {
                total += w;
                if (++accepted == n - 1) break;
            }
        }
        return static_cast<int>(total);
    }
};
