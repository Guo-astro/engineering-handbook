// LC 787. Cheapest Flights Within K Stops
#include <vector>
#include <climits>

class Solution {
public:
    int findCheapestPrice(int n, std::vector<std::vector<int>>& flights,
                          int src, int dst, int k) {
        const int INF = INT_MAX;
        std::vector<int> dist(n, INF);
        dist[src] = 0;
        for (int i = 0; i <= k; ++i) {
            // copy previous-pass view; the K-edge bound depends on it
            std::vector<int> snapshot = dist;
            for (const auto& f : flights) {
                int u = f[0], v = f[1], w = f[2];
                if (snapshot[u] == INF) continue;
                if (snapshot[u] + w < dist[v]) {
                    dist[v] = snapshot[u] + w;
                }
            }
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
};
