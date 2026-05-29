// LC 1368. Minimum Cost to Make at Least One Valid Path in a Grid
#include <vector>
#include <deque>
#include <climits>
#include <utility>

class Solution {
public:
    int minCost(std::vector<std::vector<int>>& grid) {
        int rows = (int) grid.size(), cols = (int) grid[0].size();
        int dr[5] = {0, 0, 0, 1, -1};
        int dc[5] = {0, 1, -1, 0, 0};

        std::vector<std::vector<int>> dist(rows, std::vector<int>(cols, INT_MAX));
        dist[0][0] = 0;

        std::deque<std::pair<int,int>> dq;
        dq.push_front({0, 0});
        while (!dq.empty()) {
            auto [r, c] = dq.front(); dq.pop_front();
            for (int d = 1; d <= 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                int cost = (grid[r][c] == d) ? 0 : 1;
                int nd = dist[r][c] + cost;
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    if (cost == 0) dq.push_front({nr, nc});
                    else           dq.push_back({nr, nc});
                }
            }
        }
        return dist[rows - 1][cols - 1];
    }
};
