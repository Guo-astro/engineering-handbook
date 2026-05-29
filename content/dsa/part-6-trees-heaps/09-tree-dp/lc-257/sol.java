// LC 257. Binary Tree Paths
import java.util.ArrayList;
import java.util.List;

public final class Sol {

    public static final class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    // Shape 1 of tree DP: accumulator on the call stack with backtracking.
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> out = new ArrayList<>();
        if (root == null) return out;
        walk(root, new StringBuilder(), out);
        return out;
    }

    private void walk(TreeNode node, StringBuilder path, List<String> out) {
        int len = path.length();
        if (len > 0) path.append("->");
        path.append(node.val);
        if (node.left == null && node.right == null) {
            out.add(path.toString());
        } else {
            if (node.left != null) walk(node.left, path, out);
            if (node.right != null) walk(node.right, path, out);
        }
        path.setLength(len); // backtrack so siblings see a clean prefix
    }
}
