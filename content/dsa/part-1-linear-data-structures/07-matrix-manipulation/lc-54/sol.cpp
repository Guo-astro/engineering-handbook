// LC 54. Spiral Matrix
// Walk an m x n matrix in clockwise spiral order using four shrinking
// boundaries. The two `if top <= bottom` and `if left <= right` guards
// inside the loop are mandatory: without them, odd-shaped rectangles
// re-emit the bottom row or right column. Square matrices accidentally
// work without the guards, hiding the bug. O(m*n), O(1) extra.
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        std::vector<int> out;
        if (matrix.empty() || matrix[0].empty()) return out;
        int top = 0, bottom = static_cast<int>(matrix.size()) - 1;
        int left = 0, right = static_cast<int>(matrix[0].size()) - 1;
        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; ++j) out.push_back(matrix[top][j]);
            ++top;
            for (int i = top; i <= bottom; ++i) out.push_back(matrix[i][right]);
            --right;
            if (top <= bottom) {
                for (int j = right; j >= left; --j) out.push_back(matrix[bottom][j]);
                --bottom;
            }
            if (left <= right) {
                for (int i = bottom; i >= top; --i) out.push_back(matrix[i][left]);
                ++left;
            }
        }
        return out;
    }
};
