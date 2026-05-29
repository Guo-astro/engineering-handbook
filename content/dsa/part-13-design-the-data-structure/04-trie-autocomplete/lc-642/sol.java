// LC 642. Design Search Autocomplete System (Premium)
// refreshes the cache on every path node, topk reads the cache directly.
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AutocompleteTrie {
    static final int K_CAP = 10;

    static final class Pair {
        int score;
        String word;
        Pair(int s, String w) { score = s; word = w; }
    }

    static final class Node {
        Map<Character, Node> children = new HashMap<>();
        boolean isEnd;
        List<Pair> top = new ArrayList<>();   // DESC score, ASC word, capped at K_CAP
    }

    private final Node root = new Node();
    private final Map<String, Integer> scores = new HashMap<>();

    public void input(String word, int freq) {
        scores.put(word, freq);
        Node node = root;
        insertTop(node.top, freq, word);
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            node.children.putIfAbsent(ch, new Node());
            node = node.children.get(ch);
            insertTop(node.top, freq, word);
        }
        node.isEnd = true;
    }

    public List<String> topk(String prefix, int k) {
        List<String> out = new ArrayList<>();
        if (k <= 0) return out;
        Node node = root;
        for (int i = 0; i < prefix.length(); i++) {
            Node nxt = node.children.get(prefix.charAt(i));
            if (nxt == null) return out;
            node = nxt;
        }
        int limit = Math.min(k, node.top.size());
        for (int i = 0; i < limit; i++) out.add(node.top.get(i).word);
        return out;
    }

    private static void insertTop(List<Pair> top, int score, String word) {
        for (int i = 0; i < top.size(); i++) {
            if (top.get(i).word.equals(word)) { top.remove(i); break; }
        }
        int pos = top.size();
        for (int i = 0; i < top.size(); i++) {
            Pair p = top.get(i);
            if (score > p.score || (score == p.score && word.compareTo(p.word) < 0)) {
                pos = i;
                break;
            }
        }
        top.add(pos, new Pair(score, word));
        if (top.size() > K_CAP) top.remove(top.size() - 1);
    }
}
