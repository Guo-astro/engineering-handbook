// LC 450. Delete Node in a BST
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

    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null && root.right == null) return null;  // case 1
            if (root.left == null) return root.right;                  // case 2a
            if (root.right == null) return root.left;                  // case 2b
            TreeNode succ = minNode(root.right);                       // case 3
            root.val = succ.val;
            root.right = deleteNode(root.right, succ.val);
        }
        return root;
    }

    private TreeNode minNode(TreeNode n) {
        while (n.left != null) n = n.left;
        return n;
    }
}
