// LC 297. Serialize and Deserialize Binary Tree
// Codec: preorder DFS + "#" sentinel for null children; round-trip is a same-shaped
// preorder DFS reading from an iterator over the tokens.
#include <queue>
#include <sstream>
#include <string>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Codec {
public:
    // Preorder DFS; emit value or NULL token for each slot.
    std::string serialize(TreeNode* root) {
        std::ostringstream out;
        serializeDfs(root, out, /*first=*/true);
        return out.str();
    }

    // Same preorder shape; consume one token per slot from the queue.
    TreeNode* deserialize(const std::string& data) {
        std::queue<std::string> tokens;
        std::stringstream ss(data);
        std::string tok;
        while (std::getline(ss, tok, ',')) tokens.push(tok);
        return build(tokens);
    }

private:
    static constexpr const char* kNull = "#";

    void serializeDfs(TreeNode* n, std::ostringstream& out, bool first) {
        if (!first) out << ',';
        if (!n) { out << kNull; return; }
        out << n->val;                            // visit (preorder)
        serializeDfs(n->left,  out, /*first=*/false);
        serializeDfs(n->right, out, /*first=*/false);
    }

    TreeNode* build(std::queue<std::string>& tokens) {
        if (tokens.empty()) return nullptr;
        std::string tok = tokens.front(); tokens.pop();
        if (tok == kNull) return nullptr;
        auto* node = new TreeNode(std::stoi(tok));
        node->left  = build(tokens);
        node->right = build(tokens);
        return node;
    }
};
