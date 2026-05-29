// LC 99. Recover Binary Search Tree

public final class Sol {

    public static class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;

        public TreeNode() {}

        public TreeNode(int val) {
            this.val = val;
        }

        public TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    /**
     * Recover a BST in which exactly two nodes are swapped, in O(1) space.
     *
     * Reference: J. M. Morris, "Traversing binary trees simply and cheaply",
     * Information Processing Letters 9(5):197-200, 1979.
     *
     * Layers the LC 99 "two witnesses" pattern on top of Morris inorder:
     * track prev across the visit step; capture first on the first
     * violation; keep updating second on every violation; swap at the end.
     */
    public void recoverTree(TreeNode root) {
        TreeNode first = null;
        TreeNode second = null;
        TreeNode prev = null;

        TreeNode curr = root;
        while (curr != null) {
            if (curr.left == null) {
                // Visit step.
                if (prev != null && curr.val < prev.val) {
                    if (first == null) {
                        first = prev;
                    }
                    second = curr;
                }
                prev = curr;
                curr = curr.right;
            } else {
                TreeNode pred = curr.left;
                while (pred.right != null && pred.right != curr) {
                    pred = pred.right;
                }
                if (pred.right == null) {
                    pred.right = curr;          // install thread
                    curr = curr.left;
                } else {
                    pred.right = null;          // tear down before visit
                    if (prev != null && curr.val < prev.val) {
                        if (first == null) {
                            first = prev;
                        }
                        second = curr;
                    }
                    prev = curr;
                    curr = curr.right;
                }
            }
        }

        if (first != null && second != null) {
            int tmp = first.val;
            first.val = second.val;
            second.val = tmp;
        }
    }
}
