// LC 99. Recover Binary Search Tree

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* l, TreeNode* r) : val(x), left(l), right(r) {}
};

class Solution {
public:
    // Recover a BST in which exactly two nodes are swapped, in O(1) space.
    //
    // Reference: J. M. Morris, "Traversing binary trees simply and cheaply",
    // Information Processing Letters 9(5):197-200, 1979.
    //
    // Layers the LC 99 "two witnesses" pattern on top of Morris inorder.
    void recoverTree(TreeNode* root) {
        TreeNode* first = nullptr;
        TreeNode* second = nullptr;
        TreeNode* prev = nullptr;

        TreeNode* curr = root;
        while (curr != nullptr) {
            if (curr->left == nullptr) {
                if (prev != nullptr && curr->val < prev->val) {
                    if (first == nullptr) {
                        first = prev;
                    }
                    second = curr;
                }
                prev = curr;
                curr = curr->right;
            } else {
                TreeNode* pred = curr->left;
                while (pred->right != nullptr && pred->right != curr) {
                    pred = pred->right;
                }
                if (pred->right == nullptr) {
                    pred->right = curr;          // install thread
                    curr = curr->left;
                } else {
                    pred->right = nullptr;       // tear down before visit
                    if (prev != nullptr && curr->val < prev->val) {
                        if (first == nullptr) {
                            first = prev;
                        }
                        second = curr;
                    }
                    prev = curr;
                    curr = curr->right;
                }
            }
        }

        if (first != nullptr && second != nullptr) {
            int tmp = first->val;
            first->val = second->val;
            second->val = tmp;
        }
    }
};
