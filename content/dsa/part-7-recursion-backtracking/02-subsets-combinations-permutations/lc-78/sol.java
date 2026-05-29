// LC 78. Subsets
import java.util.ArrayList;
import java.util.List;

public final class Sol {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(nums, 0, path, result);
        return result;
    }

    private void dfs(int[] nums, int start, List<Integer> path, List<List<Integer>> result) {
        result.add(new ArrayList<>(path));   // snapshot at every node
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            dfs(nums, i + 1, path, result);  // i+1 prevents reuse and reordering
            path.remove(path.size() - 1);    // undo for backtrack
        }
    }
}
