// LC: none — chapter mechanic (AVL insert with rebalance)
public final class Sol {

    static class Node {
        int key;
        Node left, right;
        int height;
        Node(int key) { this.key = key; this.height = 1; }
    }

    public static int height(Node n) { return n == null ? 0 : n.height; }

    public static int balanceFactor(Node n) {
        return height(n.left) - height(n.right);
    }

    private static void updateHeight(Node n) {
        n.height = 1 + Math.max(height(n.left), height(n.right));
    }

    private static Node rotateRight(Node y) {        // fixes LL
        Node x = y.left;
        Node t2 = x.right;
        x.right = y;
        y.left = t2;
        updateHeight(y);
        updateHeight(x);
        return x;
    }

    private static Node rotateLeft(Node x) {         // fixes RR
        Node y = x.right;
        Node t2 = y.left;
        y.left = x;
        x.right = t2;
        updateHeight(x);
        updateHeight(y);
        return y;
    }

    public static Node insert(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.key)      root.left  = insert(root.left,  key);
        else if (key > root.key) root.right = insert(root.right, key);
        else return root;                            // duplicate

        updateHeight(root);
        int bf = balanceFactor(root);

        if (bf >  1 && root.left  != null && key < root.left.key)        // LL
            return rotateRight(root);
        if (bf < -1 && root.right != null && key > root.right.key)       // RR
            return rotateLeft(root);
        if (bf >  1 && root.left  != null && key > root.left.key) {      // LR
            root.left = rotateLeft(root.left);
            return rotateRight(root);
        }
        if (bf < -1 && root.right != null && key < root.right.key) {     // RL
            root.right = rotateRight(root.right);
            return rotateLeft(root);
        }
        return root;
    }
}
