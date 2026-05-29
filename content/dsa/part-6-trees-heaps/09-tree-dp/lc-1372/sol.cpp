// LC 1372. Longest ZigZag Path in a Binary Tree
#include <utility>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Shape 3 of tree DP (diameter trick) + shape 4 (tuple return).
    // std::pair<int,int> {leftExtending, rightExtending}; pass-by-ref
    // best is the natural C++ idiom for the closure-captured global.
    int longestZigZag(TreeNode* root) {
        if (root == nullptr) return 0;
        int best = 0;
        helper(root, best);
        return best;
    }

private:
    std::pair<int, int> helper(TreeNode* node, int& best) {
        if (node == nullptr) return {-1, -1};
        auto leftPair  = helper(node->left, best);
        auto rightPair = helper(node->right, best);
        // Each child contributes the chain ending in the OTHER direction.
        int leftLen  = leftPair.second + 1;
        int rightLen = rightPair.first + 1;
        int localBest = leftLen > rightLen ? leftLen : rightLen;
        if (localBest > best) best = localBest;
        return {leftLen, rightLen};
    }
};
