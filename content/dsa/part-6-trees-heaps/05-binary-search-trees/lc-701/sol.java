// LC 701. Insert into a Binary Search Tree
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

    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left = insertIntoBST(root.left, val);
        else if (val > root.val) root.right = insertIntoBST(root.right, val);
        // Duplicate: no-op.
        return root;
    }
}
