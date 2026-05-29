// LC 297. Serialize and Deserialize Binary Tree
// Codec: preorder DFS + "#" sentinel for null children; round-trip is a same-shaped
// preorder DFS reading from an iterator over the tokens.
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringJoiner;

public final class Sol {

    static final class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public static final class Codec {

        private static final String NULL = "#";
        private static final String SEP  = ",";

        /** Preorder DFS; emit value or NULL token for each slot. */
        public String serialize(TreeNode root) {
            StringJoiner sj = new StringJoiner(SEP);
            serializeDfs(root, sj);
            return sj.toString();
        }

        private void serializeDfs(TreeNode n, StringJoiner sj) {
            if (n == null) { sj.add(NULL); return; }
            sj.add(Integer.toString(n.val));     // visit (preorder)
            serializeDfs(n.left, sj);
            serializeDfs(n.right, sj);
        }

        /** Same preorder shape; consume one token per slot from the queue. */
        public TreeNode deserialize(String data) {
            Deque<String> tokens = new ArrayDeque<>();
            for (String t : data.split(SEP)) tokens.offer(t);
            return build(tokens);
        }

        private TreeNode build(Deque<String> tokens) {
            String tok = tokens.poll();
            if (tok == null || tok.equals(NULL)) return null;
            TreeNode node = new TreeNode(Integer.parseInt(tok));
            node.left  = build(tokens);
            node.right = build(tokens);
            return node;
        }
    }
}
