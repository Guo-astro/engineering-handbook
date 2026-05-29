// LC 968. Binary Tree Cameras
// mirrors the three-state DP pattern
//  (state-machine reduction on tree).

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int minCameraCover(TreeNode* root) {
        cameras_ = 0;
        if (dfs(root) == NEEDS_COVER) cameras_++;
        return cameras_;
    }

private:
    static constexpr int NEEDS_COVER = 0;
    static constexpr int HAS_CAMERA  = 1;
    static constexpr int COVERED     = 2;

    int cameras_;

    int dfs(TreeNode* node) {
        if (node == nullptr) return COVERED;
        int l = dfs(node->left);
        int r = dfs(node->right);
        // Any child unmonitored — place a camera here.
        if (l == NEEDS_COVER || r == NEEDS_COVER) {
            cameras_++;
            return HAS_CAMERA;
        }
        // Any child holds a camera — this node is covered by it.
        if (l == HAS_CAMERA || r == HAS_CAMERA) return COVERED;
        // Both children covered, none has a camera — this node needs cover.
        return NEEDS_COVER;
    }
};
