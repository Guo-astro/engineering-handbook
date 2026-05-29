// LC 700. Search in a Binary Search Tree
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

    public TreeNode searchBST(TreeNode root, int target) {
        TreeNode cur = root;
        while (cur != null) {
            if (target == cur.val) return cur;
            cur = (target < cur.val) ? cur.left : cur.right;
        }
        return null;
    }
}
