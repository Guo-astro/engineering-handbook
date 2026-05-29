// LC 110. Balanced Binary Tree
// LC 110 Balanced Binary Tree, height-or-sentinel post-order recursion.
#include <algorithm>
#include <cstdlib>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return height(root) != -1;
    }

private:
    int height(TreeNode* node) {
        if (node == nullptr) return 0;
        int lh = height(node->left);
        if (lh == -1) return -1;
        int rh = height(node->right);
        if (rh == -1) return -1;
        if (std::abs(lh - rh) > 1) return -1;
        return 1 + std::max(lh, rh);
    }
};
