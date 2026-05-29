// LC 39. Combination Sum
// mechanism (recurse with i, not i+1, to allow reuse).
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public final class Sol {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);                          // sort enables the early break below
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(candidates, 0, target, path, result);
        return result;
    }

    private void dfs(int[] candidates, int start, int remaining,
                     List<Integer> path, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));            // snapshot when target hit exactly
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) break;         // sorted: no later candidate fits either
            path.add(candidates[i]);
            dfs(candidates, i, remaining - candidates[i], path, result); // i, not i+1
            path.remove(path.size() - 1);                 // undo for backtrack
        }
    }
}
