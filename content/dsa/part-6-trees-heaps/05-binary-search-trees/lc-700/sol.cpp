// LC 700. Search in a Binary Search Tree
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int target) {
        TreeNode* cur = root;
        while (cur) {
            if (target == cur->val) return cur;
            cur = (target < cur->val) ? cur->left : cur->right;
        }
        return nullptr;
    }
};
