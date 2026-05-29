// LC 212. Word Search II
// Trie-accelerated DFS over the grid; missing trie child = instant
// backtrack. After finding a word, clear the stored word and prune
// dead branches upward.
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> findWords(std::vector<std::vector<char>>& board,
                                       std::vector<std::string>& words) {
        Node root;
        for (const auto& w : words) {
            Node* node = &root;
            for (char ch : w) {
                auto& nxt = node->children[ch];
                if (!nxt) nxt = std::make_unique<Node>();
                node = nxt.get();
            }
            node->word = w;
        }

        std::vector<std::string> found;
        for (int r = 0; r < (int)board.size(); ++r) {
            for (int c = 0; c < (int)board[0].size(); ++c) {
                dfs(board, r, c, &root, found);
            }
        }
        return found;
    }

private:
    struct Node {
        std::unordered_map<char, std::unique_ptr<Node>> children;
        std::string word;
    };

    void dfs(std::vector<std::vector<char>>& board, int r, int c,
             Node* parent, std::vector<std::string>& found) {
        char ch = board[r][c];
        auto it = parent->children.find(ch);
        if (it == parent->children.end()) return;
        Node* node = it->second.get();
        if (!node->word.empty()) {
            found.push_back(node->word);
            node->word.clear();
        }
        board[r][c] = '#';
        const int dr[4] = {-1, 1, 0, 0};
        const int dc[4] = {0, 0, -1, 1};
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < (int)board.size()
                    && nc >= 0 && nc < (int)board[0].size()
                    && board[nr][nc] != '#') {
                dfs(board, nr, nc, node, found);
            }
        }
        board[r][c] = ch;
        if (node->children.empty()) {
            parent->children.erase(it);
        }
    }
};
