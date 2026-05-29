// LC 78. Subsets
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        dfs(nums, 0, path, result);
        return result;
    }

private:
    void dfs(const std::vector<int>& nums, int start,
             std::vector<int>& path,
             std::vector<std::vector<int>>& result) {
        result.push_back(path);                  // snapshot at every node
        for (int i = start; i < (int)nums.size(); ++i) {
            path.push_back(nums[i]);
            dfs(nums, i + 1, path, result);      // i+1 prevents reuse and reordering
            path.pop_back();                     // undo for backtrack
        }
    }
};
