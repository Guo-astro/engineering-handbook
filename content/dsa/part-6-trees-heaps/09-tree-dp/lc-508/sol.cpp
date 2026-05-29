// LC 508. Most Frequent Subtree Sum
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Shape 2 of tree DP: post-order returns subtree sum; counts side
    // accumulator records every sum. C++'s int& best parameter is the
    // pass-by-reference equivalent of Java's int[] best wrapper.
    std::vector<int> findFrequentTreeSum(TreeNode* root) {
        std::vector<int> res;
        if (root == nullptr) return res;
        std::unordered_map<int, int> counts;
        int best = 0;
        subtreeSum(root, counts, best);
        for (const auto& kv : counts) {
            if (kv.second == best) res.push_back(kv.first);
        }
        return res;
    }

private:
    int subtreeSum(TreeNode* node, std::unordered_map<int, int>& counts, int& best) {
        if (node == nullptr) return 0;
        int s = node->val
              + subtreeSum(node->left, counts, best)
              + subtreeSum(node->right, counts, best);
        int c = ++counts[s];
        if (c > best) best = c;
        return s;
    }
};
