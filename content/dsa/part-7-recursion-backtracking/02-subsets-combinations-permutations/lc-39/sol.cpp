// LC 39. Combination Sum
// mechanism (recurse with i, not i+1, to allow reuse).
#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum(std::vector<int>& candidates, int target) {
        std::sort(candidates.begin(), candidates.end());   // sort enables the early break below
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        dfs(candidates, 0, target, path, result);
        return result;
    }

private:
    void dfs(const std::vector<int>& candidates, int start, int remaining,
             std::vector<int>& path,
             std::vector<std::vector<int>>& result) {
        if (remaining == 0) {
            result.push_back(path);                        // snapshot when target hit exactly
            return;
        }
        for (int i = start; i < (int)candidates.size(); ++i) {
            if (candidates[i] > remaining) break;          // sorted: no later candidate fits either
            path.push_back(candidates[i]);
            dfs(candidates, i, remaining - candidates[i], path, result); // i, not i+1
            path.pop_back();                               // undo for backtrack
        }
    }
};
