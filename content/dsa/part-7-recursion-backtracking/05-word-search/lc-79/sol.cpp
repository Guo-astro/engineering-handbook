// LC 79. Word Search
#include <vector>
#include <string>

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, const std::string& word) {
        if (board.empty() || board[0].empty() || word.empty()) return false;
        int rows = static_cast<int>(board.size());
        int cols = static_cast<int>(board[0].size());
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (board[r][c] == word[0] && dfs(board, r, c, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    bool dfs(std::vector<std::vector<char>>& board, int r, int c, int k,
             const std::string& word) {
        if (k == static_cast<int>(word.size())) return true;
        int rows = static_cast<int>(board.size());
        int cols = static_cast<int>(board[0].size());
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[k]) {
            return false;
        }
        char saved = board[r][c];
        board[r][c] = '#';   // sentinel never matches a real word char
        bool found = dfs(board, r + 1, c, k + 1, word)
                  || dfs(board, r - 1, c, k + 1, word)
                  || dfs(board, r, c + 1, k + 1, word)
                  || dfs(board, r, c - 1, k + 1, word);
        board[r][c] = saved; // restore on backtrack
        return found;
    }
};
