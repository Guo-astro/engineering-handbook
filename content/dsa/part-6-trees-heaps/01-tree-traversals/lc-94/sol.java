// LC 94. Binary Tree Inorder Traversal
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;

public final class Sol {

    static final class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val; this.left = left; this.right = right;
        }
    }

    /** Recursive inorder — the canonical LC 94 entry point. */
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        inorder(root, out);
        return out;
    }

    private void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);                          // visit
        inorder(n.right, out);
    }

    /** Iterative inorder via ArrayDeque (preferred over legacy java.util.Stack,
     *  which extends Vector and is synchronized). Push left chain, pop, pivot right.
     */
    public List<Integer> inorderIterative(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            out.add(cur.val);
            cur = cur.right;                     // pivot to right subtree
        }
        return out;
    }

    /** Iterative preorder. Push right BEFORE left so left pops next. */
    public List<Integer> preorderIterative(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            out.add(n.val);
            if (n.right != null) stack.push(n.right);
            if (n.left != null)  stack.push(n.left);
        }
        return out;
    }

    /** Iterative postorder via the two-stack / reverse trick. */
    public List<Integer> postorderIterative(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            out.add(n.val);
            if (n.left != null)  stack.push(n.left);
            if (n.right != null) stack.push(n.right);
        }
        Collections.reverse(out);
        return out;
    }
}
