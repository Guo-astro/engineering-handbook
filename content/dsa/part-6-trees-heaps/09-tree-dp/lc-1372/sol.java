// LC 1372. Longest ZigZag Path in a Binary Tree
public final class Sol {

    public static final class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    // Shape 3 of tree DP (diameter trick) + shape 4 (tuple return).
    // int[2] {leftExtending, rightExtending} is the canonical Java
    // idiom for tuple returns; -1 in both slots is the null sentinel.
    public int longestZigZag(TreeNode root) {
        if (root == null) return 0;
        int[] best = new int[]{0};
        helper(root, best);
        return best[0];
    }

    private int[] helper(TreeNode node, int[] best) {
        if (node == null) return new int[]{-1, -1};
        int[] leftPair  = helper(node.left, best);
        int[] rightPair = helper(node.right, best);
        // Each child contributes the chain ending in the OTHER direction.
        int leftLen  = leftPair[1] + 1;
        int rightLen = rightPair[0] + 1;
        int localBest = leftLen > rightLen ? leftLen : rightLen;
        if (localBest > best[0]) best[0] = localBest;
        return new int[]{leftLen, rightLen};
    }
}
