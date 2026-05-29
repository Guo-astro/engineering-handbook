// LC 450. Delete Node in a BST
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            if (!root->left && !root->right) {
                delete root;
                return nullptr;                              // case 1
            }
            if (!root->left) {
                TreeNode* r = root->right;
                delete root;
                return r;                                    // case 2a
            }
            if (!root->right) {
                TreeNode* l = root->left;
                delete root;
                return l;                                    // case 2b
            }
            TreeNode* succ = minNode(root->right);           // case 3
            root->val = succ->val;
            root->right = deleteNode(root->right, succ->val);
        }
        return root;
    }

private:
    TreeNode* minNode(TreeNode* n) {
        while (n->left) n = n->left;
        return n;
    }
};
