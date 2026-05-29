// LC 701. Insert into a Binary Search Tree
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);
        if (val < root->val) root->left = insertIntoBST(root->left, val);
        else if (val > root->val) root->right = insertIntoBST(root->right, val);
        // Duplicate: no-op.
        return root;
    }
};
