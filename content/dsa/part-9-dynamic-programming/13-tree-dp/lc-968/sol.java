// LC 968. Binary Tree Cameras
// mirrors the three-state DP pattern from research
// §5.6 (state-machine reduction on tree).
public final class Sol {

    public static final class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    // State codes returned by dfs:
    //   0 = NEEDS_COVER, 1 = HAS_CAMERA, 2 = COVERED
    private static final int NEEDS_COVER = 0;
    private static final int HAS_CAMERA  = 1;
    private static final int COVERED     = 2;

    private int cameras;

    public int minCameraCover(TreeNode root) {
        cameras = 0;
        if (dfs(root) == NEEDS_COVER) cameras++;
        return cameras;
    }

    private int dfs(TreeNode node) {
        if (node == null) return COVERED;
        int l = dfs(node.left);
        int r = dfs(node.right);
        // Any child unmonitored — place a camera here.
        if (l == NEEDS_COVER || r == NEEDS_COVER) {
            cameras++;
            return HAS_CAMERA;
        }
        // Any child holds a camera — this node is covered by it.
        if (l == HAS_CAMERA || r == HAS_CAMERA) return COVERED;
        // Both children covered, none has a camera — this node needs cover.
        return NEEDS_COVER;
    }
}
