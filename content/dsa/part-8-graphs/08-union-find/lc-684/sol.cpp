// LC 684. Redundant Connection
#include <vector>

class DSU {
public:
    std::vector<int> parent;
    std::vector<int> rank_;
    DSU(int n) : parent(n + 1), rank_(n + 1, 0) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        if (rank_[rx] < rank_[ry]) std::swap(rx, ry);
        parent[ry] = rx;
        if (rank_[rx] == rank_[ry]) rank_[rx]++;
        return true;
    }
};

std::vector<int> findRedundantConnection(std::vector<std::vector<int>>& edges) {
    int n = edges.size();
    DSU dsu(n);
    for (auto& e : edges) {
        if (!dsu.unite(e[0], e[1])) return e;
    }
    return {};
}
