// LC 211. Design Add and Search Words Data Structure
// LC 211 test sequence
// [addWord("bad"), addWord("dad"), addWord("mad"), search("pad")=false,
//  search("bad")=true, search(".ad")=true, search("b..")=true] passes.
public final class Sol {

    private static final class Node {
        Node[] children = new Node[26];
        boolean isEnd;
    }

    private final Node root;

    public Sol() {
        root = new Node();
    }

    public void addWord(String word) {
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
        return dfs(root, word, 0);
    }

    private boolean dfs(Node node, String word, int i) {
        if (i == word.length()) return node.isEnd;
        char ch = word.charAt(i);
        if (ch == '.') {
            for (Node child : node.children) {
                if (child != null && dfs(child, word, i + 1)) return true;
            }
            return false;
        }
        Node nxt = node.children[ch - 'a'];
        if (nxt == null) return false;
        return dfs(nxt, word, i + 1);
    }
}
