// LC 1042. Flower Planting With No Adjacent
// NOT a 2-coloring: 4 flower types over a max-degree-3 graph (greedy works).
#include <vector>

class Solution {
public:
    std::vector<int> gardenNoAdj(int n, std::vector<std::vector<int>>& paths) {
        std::vector<std::vector<int>> graph(n + 1);   // 1-indexed
        for (auto& p : paths) {
            graph[p[0]].push_back(p[1]);
            graph[p[1]].push_back(p[0]);
        }

        std::vector<int> answer(n + 1, 0);            // 0 = unassigned; flowers 1..4
        for (int u = 1; u <= n; ++u) {
            bool used[5] = {false, false, false, false, false};
            for (int v : graph[u]) {
                if (answer[v] != 0) used[answer[v]] = true;
            }
            for (int flower = 1; flower <= 4; ++flower) {
                if (!used[flower]) {
                    answer[u] = flower;
                    break;
                }
            }
        }
        return std::vector<int>(answer.begin() + 1, answer.end());
    }
};
