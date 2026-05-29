// LC 257. Binary Tree Paths
#include <string>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Shape 1 of tree DP: accumulator on the call stack with backtracking.
    std::vector<std::string> binaryTreePaths(TreeNode* root) {
        std::vector<std::string> out;
        if (root == nullptr) return out;
        std::string path;
        walk(root, path, out);
        return out;
    }

private:
    void walk(TreeNode* node, std::string& path, std::vector<std::string>& out) {
        std::size_t saved = path.size();
        if (!path.empty()) path += "->";
        path += std::to_string(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            out.push_back(path);
        } else {
            if (node->left != nullptr) walk(node->left, path, out);
            if (node->right != nullptr) walk(node->right, path, out);
        }
        path.resize(saved); // backtrack so siblings see a clean prefix
    }
};
