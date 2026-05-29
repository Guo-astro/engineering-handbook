// LC 547. Number of Provinces
#include <vector>
#include <queue>

class Solution {
public:
    int findCircleNum(std::vector<std::vector<int>>& isConnected) {
        const int n = static_cast<int>(isConnected.size());
        std::vector<bool> visited(n, false);
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++count;
                std::queue<int> q;
                q.push(i);
                visited[i] = true;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v = 0; v < n; ++v) {
                        if (isConnected[u][v] == 1 && !visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }
            }
        }
        return count;
    }
};
