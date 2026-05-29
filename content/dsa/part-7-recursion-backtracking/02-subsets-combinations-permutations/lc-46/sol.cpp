// LC 46. Permutations
// mechanism pseudocode and §5.3.
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        std::vector<bool> used(nums.size(), false);
        dfs(nums, used, path, result);
        return result;
    }

private:
    void dfs(const std::vector<int>& nums,
             std::vector<bool>& used,
             std::vector<int>& path,
             std::vector<std::vector<int>>& result) {
        if (path.size() == nums.size()) {
            result.push_back(path);                   // snapshot only at full-length leaves
            return;
        }
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (used[i]) continue;                    // element already in path; skip
            used[i] = true;
            path.push_back(nums[i]);
            dfs(nums, used, path, result);
            path.pop_back();                          // undo for backtrack
            used[i] = false;
        }
    }
};
