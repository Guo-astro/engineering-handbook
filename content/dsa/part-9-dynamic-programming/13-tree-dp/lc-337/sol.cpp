// LC 337. House Robber III
// mirrors the two-state tuple-return
// pattern (pair-return state machine on tree).
#include <algorithm>
#include <utility>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int rob(TreeNode* root) {
        auto [robRoot, skipRoot] = helper(root);
        return std::max(robRoot, skipRoot);
    }

private:
    // Returns {robThis, skipThis}. std::pair<int,int> is the canonical C++
    // idiom for a 2-tuple per-node state on tree DP.
    std::pair<int, int> helper(TreeNode* node) {
        if (node == nullptr) return {0, 0};
        auto [robL, skipL] = helper(node->left);
        auto [robR, skipR] = helper(node->right);
        // robThis: include this node; both children MUST be skipped.
        int robThis  = node->val + skipL + skipR;
        // skipThis: take the better state at each child independently.
        int skipThis = std::max(robL, skipL) + std::max(robR, skipR);
        return {robThis, skipThis};
    }
};
