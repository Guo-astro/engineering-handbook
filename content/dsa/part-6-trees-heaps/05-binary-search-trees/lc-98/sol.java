// LC 98. Validate Binary Search Tree
public final class Sol {
    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { this.val = v; }
        TreeNode(int v, TreeNode l, TreeNode r) {
            this.val = v;
            this.left = l;
            this.right = r;
        }
    }

    public boolean isValidBST(TreeNode root) {
        return check(root, null, null);
    }

    // Boxed Integer sentinels admit null on the unbounded side; this avoids
    // the Integer.MIN_VALUE / Integer.MAX_VALUE collision with real keys.
    private boolean check(TreeNode n, Integer lo, Integer hi) {
        if (n == null) return true;
        if (lo != null && n.val <= lo) return false;
        if (hi != null && n.val >= hi) return false;
        return check(n.left, lo, n.val) && check(n.right, n.val, hi);
    }
}
