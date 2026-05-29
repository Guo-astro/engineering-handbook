// LC 588. Design In-Memory File System (LeetCode Premium)
// Generalizes the dual-structure pattern: trie of std::map nodes.
#include <map>
#include <memory>
#include <sstream>
#include <string>
#include <vector>

class FileSystem {
public:
    std::vector<std::string> ls(const std::string& path) {
        Node* node = walk(path);
        if (node->isFile) {
            // ls on a file path returns the basename only
            std::string base = path.substr(path.find_last_of('/') + 1);
            return {base};
        }
        std::vector<std::string> out;
        for (const auto& [name, _] : node->children) out.push_back(name);
        return out;  // std::map iterates in alphabetical order
    }

    void mkdir(const std::string& path) {
        walk(path);
    }

    void addContentToFile(const std::string& filePath, const std::string& content) {
        Node* node = walk(filePath);
        node->isFile = true;
        node->content += content;
    }

    std::string readContentFromFile(const std::string& filePath) {
        return walk(filePath)->content;
    }

private:
    struct Node {
        std::map<std::string, std::unique_ptr<Node>> children;
        bool isFile = false;
        std::string content;
    };

    Node* walk(const std::string& path) {
        Node* node = &root_;
        if (path == "/") return node;
        std::stringstream ss(path.substr(1));
        std::string part;
        while (std::getline(ss, part, '/')) {
            auto it = node->children.find(part);
            if (it == node->children.end()) {
                auto fresh = std::make_unique<Node>();
                Node* raw = fresh.get();
                node->children.emplace(part, std::move(fresh));
                node = raw;
            } else {
                node = it->second.get();
            }
        }
        return node;
    }

    Node root_;
};
