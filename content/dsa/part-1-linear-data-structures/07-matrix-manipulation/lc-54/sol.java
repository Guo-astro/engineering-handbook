// LC 54. Spiral Matrix
// Walk an m x n matrix in clockwise spiral order using four shrinking
// boundaries. The two `if top <= bottom` and `if left <= right` guards
// inside the loop are mandatory: without them, odd-shaped rectangles
// re-emit the bottom row or right column. Square matrices accidentally
// work without the guards, hiding the bug. O(m*n), O(1) extra.
import java.util.ArrayList;
import java.util.List;

public final class Sol {

    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> out = new ArrayList<>();
        if (matrix.length == 0 || matrix[0].length == 0) return out;
        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;
        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; j++) out.add(matrix[top][j]);
            top++;
            for (int i = top; i <= bottom; i++) out.add(matrix[i][right]);
            right--;
            if (top <= bottom) {
                for (int j = right; j >= left; j--) out.add(matrix[bottom][j]);
                bottom--;
            }
            if (left <= right) {
                for (int i = bottom; i >= top; i--) out.add(matrix[i][left]);
                left++;
            }
        }
        return out;
    }

    private Sol() {}
}
