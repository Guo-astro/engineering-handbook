// LC 743. Network Delay Time
#include <vector>
#include <queue>
#include <climits>
#include <utility>

class Solution {
public:
    int networkDelayTime(std::vector<std::vector<int>>& times, int n, int k) {
        std::vector<std::vector<std::pair<int,int>>> adj(n + 1);
        for (auto& e : times) adj[e[0]].push_back({e[1], e[2]});

        std::vector<int> dist(n + 1, INT_MAX);
        dist[k] = 0;

        // Min-heap on (dist, node). std::greater<> flips C++'s default
        // max-heap. Forgetting it ships a max-heap that returns wrong answers.
        using PI = std::pair<int,int>;
        std::priority_queue<PI, std::vector<PI>, std::greater<PI>> pq;
        pq.push({0, k});

        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;                   // lazy-deletion
            for (auto [v, w] : adj[u]) {
                long long nd = (long long) d + w;
                if (nd < dist[v]) {
                    dist[v] = (int) nd;
                    pq.push({(int) nd, v});
                }
            }
        }

        int longest = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INT_MAX) return -1;
            if (dist[i] > longest) longest = dist[i];
        }
        return longest;
    }
};
