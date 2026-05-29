// LC 337. House Robber III
// mirrors the two-state tuple-return pattern from
//  (pair-return state machine on tree).
public final class Sol {

    public static final class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    // Helper returns int[2] {robThis, skipThis} — the canonical Java idiom
    // for tuple returns, no boxing, fits in a single allocation per node.
    public int rob(TreeNode root) {
        int[] r = helper(root);
        return Math.max(r[0], r[1]);
    }

    private int[] helper(TreeNode node) {
        if (node == null) return new int[]{0, 0};
        int[] left  = helper(node.left);
        int[] right = helper(node.right);
        // robThis: take this node's value; both children MUST be skipped.
        int robThis  = node.val + left[1] + right[1];
        // skipThis: take the better of (rob, skip) at each child independently.
        int skipThis = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{robThis, skipThis};
    }
}
