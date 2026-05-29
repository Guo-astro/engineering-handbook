// LC 208. Implement Trie (Prefix Tree)
public final class Sol {

    private static final class Node {
        Node[] children = new Node[26];
        boolean isEnd;
    }

    private final Node root;

    public Sol() {
        root = new Node();
    }

    public void insert(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new Node();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        Node node = walk(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return walk(prefix) != null;
    }

    private Node walk(String s) {
        Node node = root;
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            Node nxt = node.children[idx];
            if (nxt == null) return null;
            node = nxt;
        }
        return node;
    }
}
