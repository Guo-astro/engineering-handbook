// LC 46. Permutations
// mechanism pseudocode and §5.3.
import java.util.ArrayList;
import java.util.List;

public final class Sol {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        dfs(nums, used, path, result);
        return result;
    }

    private void dfs(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));   // snapshot only at full-length leaves
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;               // element already in path; skip
            used[i] = true;
            path.add(nums[i]);
            dfs(nums, used, path, result);
            path.remove(path.size() - 1);        // undo for backtrack
            used[i] = false;
        }
    }
}
