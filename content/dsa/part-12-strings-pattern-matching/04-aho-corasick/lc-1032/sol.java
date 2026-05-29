// LC 1032. Stream of Characters

import java.util.*;

public class StreamChecker {
    private final List<Map<Character, Integer>> children = new ArrayList<>();
    private final List<Integer> fail = new ArrayList<>();
    private final List<Boolean> hasOutput = new ArrayList<>();
    private int node = 0;  // current automaton state

    public StreamChecker(String[] words) {
        children.add(new HashMap<>());
        fail.add(0);
        hasOutput.add(false);

        // 1) Build the trie.
        for (String pat : words) {
            int cur = 0;
            for (int i = 0; i < pat.length(); i++) {
                char ch = pat.charAt(i);
                Integer nxt = children.get(cur).get(ch);
                if (nxt == null) {
                    nxt = children.size();
                    children.add(new HashMap<>());
                    fail.add(0);
                    hasOutput.add(false);
                    children.get(cur).put(ch, nxt);
                }
                cur = nxt;
            }
            hasOutput.set(cur, true);
        }

        // 2) Build failure links via BFS.
        Deque<Integer> queue = new ArrayDeque<>();
        for (Map.Entry<Character, Integer> e : children.get(0).entrySet()) {
            fail.set(e.getValue(), 0);
            queue.offer(e.getValue());
        }
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (Map.Entry<Character, Integer> e : children.get(u).entrySet()) {
                char ch = e.getKey();
                int v = e.getValue();
                queue.offer(v);
                int f = fail.get(u);
                while (f != 0 && !children.get(f).containsKey(ch)) f = fail.get(f);
                int fv = children.get(f).getOrDefault(ch, 0);
                if (fv == v) fv = 0;
                fail.set(v, fv);
                // Output inheritance: a pattern ending on the failure
                // chain also ends here.
                if (hasOutput.get(fail.get(v))) hasOutput.set(v, true);
            }
        }
    }

    public boolean query(char letter) {
        while (node != 0 && !children.get(node).containsKey(letter)) {
            node = fail.get(node);
        }
        node = children.get(node).getOrDefault(letter, 0);
        return hasOutput.get(node);
    }
}
