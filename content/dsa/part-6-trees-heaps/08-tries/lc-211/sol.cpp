// LC 211. Design Add and Search Words Data Structure
// '.' matches any one lowercase letter; LC 211 caps queries at 2 dots
// so worst case is bounded at 26^2 paths per search.
#include <array>
#include <memory>
#include <string>

class WordDictionary {
public:
    WordDictionary() : root_(std::make_unique<Node>()) {}

    void addWord(const std::string& word) {
        Node* node = root_.get();
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) {
                node->children[idx] = std::make_unique<Node>();
            }
            node = node->children[idx].get();
        }
        node->isEnd = true;
    }

    bool search(const std::string& word) const {
        return dfs(root_.get(), word, 0);
    }

private:
    struct Node {
        std::array<std::unique_ptr<Node>, 26> children{};
        bool isEnd = false;
    };

    bool dfs(const Node* node, const std::string& word, size_t i) const {
        if (i == word.size()) return node->isEnd;
        char ch = word[i];
        if (ch == '.') {
            for (const auto& child : node->children) {
                if (child && dfs(child.get(), word, i + 1)) return true;
            }
            return false;
        }
        const Node* nxt = node->children[ch - 'a'].get();
        if (!nxt) return false;
        return dfs(nxt, word, i + 1);
    }

    std::unique_ptr<Node> root_;
};
