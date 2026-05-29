// LC 124. Binary Tree Maximum Path Sum
#include <algorithm>
#include <climits>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        best_ = INT_MIN;
        gain(root);
        return best_;
    }

private:
    int best_;

    int gain(TreeNode* node) {
        if (node == nullptr) return 0;
        int leftGain  = std::max(gain(node->left),  0);
        int rightGain = std::max(gain(node->right), 0);
        // Bent path through node — compared to global, NOT returned.
        int bent = node->val + leftGain + rightGain;
        if (bent > best_) best_ = bent;
        // Straight-down path returned to parent.
        return node->val + std::max(leftGain, rightGain);
    }
};
