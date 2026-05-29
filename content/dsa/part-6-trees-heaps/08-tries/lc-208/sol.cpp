// LC 208. Implement Trie (Prefix Tree)
#include <array>
#include <memory>
#include <string>

class Trie {
public:
    Trie() : root_(std::make_unique<Node>()) {}

    void insert(const std::string& word) {
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
        const Node* node = walk(word);
        return node != nullptr && node->isEnd;
    }

    bool startsWith(const std::string& prefix) const {
        return walk(prefix) != nullptr;
    }

private:
    struct Node {
        std::array<std::unique_ptr<Node>, 26> children{};
        bool isEnd = false;
    };

    const Node* walk(const std::string& s) const {
        const Node* node = root_.get();
        for (char ch : s) {
            int idx = ch - 'a';
            const Node* nxt = node->children[idx].get();
            if (!nxt) return nullptr;
            node = nxt;
        }
        return node;
    }

    std::unique_ptr<Node> root_;
};
