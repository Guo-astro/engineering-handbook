// LC 124. Binary Tree Maximum Path Sum
public final class Sol {

    public static final class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    private int best;

    public int maxPathSum(TreeNode root) {
        best = Integer.MIN_VALUE;
        gain(root);
        return best;
    }

    // Returns the best straight-down path ending at `node`, extending into
    // at most one subtree. Updates `best` with the bent-through-this-node
    // path before returning.
    private int gain(TreeNode node) {
        if (node == null) return 0;
        int leftGain  = Math.max(gain(node.left),  0);
        int rightGain = Math.max(gain(node.right), 0);
        // Bent path through node — compared to global, NOT returned.
        int bent = node.val + leftGain + rightGain;
        if (bent > best) best = bent;
        // Straight-down path returned to parent.
        return node.val + Math.max(leftGain, rightGain);
    }
}
