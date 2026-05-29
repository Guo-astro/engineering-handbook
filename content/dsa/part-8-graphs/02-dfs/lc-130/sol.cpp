// LC 130. Surrounded Regions
#include <vector>

class Solution {
public:
    void solve(std::vector<std::vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        int m = (int)board.size(), n = (int)board[0].size();

        for (int r = 0; r < m; ++r) {
            dfs(board, r, 0, m, n);
            dfs(board, r, n - 1, m, n);
        }
        for (int c = 0; c < n; ++c) {
            dfs(board, 0, c, m, n);
            dfs(board, m - 1, c, m, n);
        }
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == '#') board[r][c] = 'O';
            }
        }
    }

private:
    void dfs(std::vector<std::vector<char>>& b, int r, int c, int m, int n) {
        if (r < 0 || r >= m || c < 0 || c >= n || b[r][c] != 'O') return;
        b[r][c] = '#';
        dfs(b, r + 1, c, m, n);
        dfs(b, r - 1, c, m, n);
        dfs(b, r, c + 1, m, n);
        dfs(b, r, c - 1, m, n);
    }
};
