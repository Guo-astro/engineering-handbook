// LC 642. Design Search Autocomplete System (Premium)
// cache via std::vector<std::pair<int, std::string>>, sorted DESC score
// then ASC word, capped at K_CAP.
#include <algorithm>
#include <memory>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class AutocompleteTrie {
public:
    static constexpr int K_CAP = 10;

    AutocompleteTrie() : root_(std::make_unique<Node>()) {}

    void input(const std::string& word, int freq) {
        scores_[word] = freq;
        Node* node = root_.get();
        insertTop(node->top, freq, word);
        for (char ch : word) {
            auto& slot = node->children[ch];
            if (!slot) slot = std::make_unique<Node>();
            node = slot.get();
            insertTop(node->top, freq, word);
        }
        node->isEnd = true;
    }

    std::vector<std::string> topk(const std::string& prefix, int k) const {
        std::vector<std::string> out;
        if (k <= 0) return out;
        const Node* node = root_.get();
        for (char ch : prefix) {
            auto it = node->children.find(ch);
            if (it == node->children.end()) return out;
            node = it->second.get();
        }
        int limit = std::min<int>(k, static_cast<int>(node->top.size()));
        for (int i = 0; i < limit; i++) out.push_back(node->top[i].second);
        return out;
    }

private:
    struct Node {
        std::unordered_map<char, std::unique_ptr<Node>> children;
        bool isEnd = false;
        // (score, word) DESC by score, ASC by word; capped at K_CAP.
        std::vector<std::pair<int, std::string>> top;
    };

    static void insertTop(std::vector<std::pair<int, std::string>>& top,
                          int score, const std::string& word) {
        for (auto it = top.begin(); it != top.end(); ++it) {
            if (it->second == word) { top.erase(it); break; }
        }
        auto pos = top.end();
        for (auto it = top.begin(); it != top.end(); ++it) {
            if (score > it->first || (score == it->first && word < it->second)) {
                pos = it;
                break;
            }
        }
        top.insert(pos, {score, word});
        if (static_cast<int>(top.size()) > K_CAP) top.pop_back();
    }

    std::unique_ptr<Node> root_;
    std::unordered_map<std::string, int> scores_;
};
