// LC 98. Validate Binary Search Tree
#include <climits>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return check(root, LLONG_MIN, LLONG_MAX);
    }

private:
    // long long sentinels strictly bracket the int key range, so legitimate
    // INT_MIN / INT_MAX node values never collide with the bounds.
    bool check(TreeNode* n, long long lo, long long hi) {
        if (!n) return true;
        if ((long long)n->val <= lo || (long long)n->val >= hi) return false;
        return check(n->left, lo, (long long)n->val)
            && check(n->right, (long long)n->val, hi);
    }
};
