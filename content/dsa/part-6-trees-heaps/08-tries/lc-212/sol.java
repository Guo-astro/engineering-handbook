// LC 212. Word Search II
// board=[[o,a,a,n],[e,t,a,e],[i,h,k,r],[i,f,l,v]],
// words=[oath,pea,eat,rain] returns [oath, eat].
//
// Trie-accelerated DFS: a single board sweep advances both the cell
// pointer and the trie node pointer; a missing trie child prunes the
// entire prefix-sharing subtree in O(1). After finding a word, clear
// the leaf's stored word to suppress re-finding.
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class Sol {

    private static final class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        String word;
    }

    private char[][] board;
    private List<String> found;

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char ch : w.toCharArray()) {
                node = node.children.computeIfAbsent(ch, k -> new TrieNode());
            }
            node.word = w;
        }

        this.board = board;
        this.found = new ArrayList<>();
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                dfs(r, c, root);
            }
        }
        return found;
    }

    private void dfs(int r, int c, TrieNode parent) {
        char ch = board[r][c];
        TrieNode node = parent.children.get(ch);
        if (node == null) return;
        if (node.word != null) {
            found.add(node.word);
            node.word = null;
        }
        board[r][c] = '#';
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < board.length
                    && nc >= 0 && nc < board[0].length
                    && board[nr][nc] != '#') {
                dfs(nr, nc, node);
            }
        }
        board[r][c] = ch;
        if (node.children.isEmpty()) {
            parent.children.remove(ch);
        }
    }
}
