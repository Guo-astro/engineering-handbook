// LC 48. Rotate Image
// Rotate an n x n matrix 90 degrees clockwise in place via two passes:
// transpose along the main diagonal, then reverse each row. The transpose
// inner loop must start at j = i + 1 or each off-diagonal pair gets
// swapped twice, returning the matrix to its original state.
// O(n^2) time, O(1) space.
#include <vector>
#include <algorithm>
#include <utility>

class Solution {
public:
    void rotate(std::vector<std::vector<int>>& matrix) {
        int n = static_cast<int>(matrix.size());
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (auto& row : matrix) {
            std::reverse(row.begin(), row.end());
        }
    }
};
