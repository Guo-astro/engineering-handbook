// LC 994. Rotting Oranges
#include <vector>
#include <queue>
#include <tuple>

class Solution {
public:
    int orangesRotting(std::vector<std::vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int rows = (int)grid.size();
        int cols = (int)grid[0].size();
        std::queue<std::tuple<int,int,int>> q;
        int fresh = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 2) q.emplace(r, c, 0);
                else if (grid[r][c] == 1) ++fresh;
            }
        }
        if (fresh == 0) return 0;
        int minutes = 0;
        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};
        while (!q.empty()) {
            auto [r, c, t] = q.front();
            q.pop();
            minutes = t;
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    --fresh;
                    q.emplace(nr, nc, t + 1);
                }
            }
        }
        return fresh == 0 ? minutes : -1;
    }
};
