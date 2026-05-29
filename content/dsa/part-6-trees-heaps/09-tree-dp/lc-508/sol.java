// LC 508. Most Frequent Subtree Sum
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class Sol {

    public static final class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    // Shape 2 of tree DP: post-order returns the subtree sum; a side
    // accumulator (the counts map) records every sum we produce. The
    // single-element int[] best is the canonical Java idiom for mutating
    // a primitive from inside a recursive helper without a class field.
    public int[] findFrequentTreeSum(TreeNode root) {
        if (root == null) return new int[0];
        Map<Integer, Integer> counts = new HashMap<>();
        int[] best = new int[]{0};
        subtreeSum(root, counts, best);
        List<Integer> modes = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            if (e.getValue() == best[0]) modes.add(e.getKey());
        }
        int[] res = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) res[i] = modes.get(i);
        return res;
    }

    private int subtreeSum(TreeNode node, Map<Integer, Integer> counts, int[] best) {
        if (node == null) return 0;
        int s = node.val
              + subtreeSum(node.left, counts, best)
              + subtreeSum(node.right, counts, best);
        int c = counts.getOrDefault(s, 0) + 1;
        counts.put(s, c);
        if (c > best[0]) best[0] = c;
        return s;
    }
}
