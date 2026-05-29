// LC 200. Number of Islands
#include <vector>
#include <queue>
#include <utility>

class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        const int rows = static_cast<int>(grid.size());
        const int cols = static_cast<int>(grid[0].size());
        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};
        int count = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == '1') {
                    ++count;
                    std::queue<std::pair<int,int>> q;
                    q.push({r, c});
                    grid[r][c] = '0';
                    while (!q.empty()) {
                        auto [cr, cc] = q.front(); q.pop();
                        for (int k = 0; k < 4; ++k) {
                            int nr = cr + dr[k], nc = cc + dc[k];
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                                && grid[nr][nc] == '1') {
                                grid[nr][nc] = '0';
                                q.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
};
