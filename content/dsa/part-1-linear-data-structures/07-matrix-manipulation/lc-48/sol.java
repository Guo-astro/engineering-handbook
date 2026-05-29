// LC 48. Rotate Image
// Rotate an n x n matrix 90 degrees clockwise in place via two passes:
// transpose along the main diagonal, then reverse each row. The transpose
// inner loop must start at j = i + 1 or each off-diagonal pair gets
// swapped twice, returning the matrix to its original state.
// O(n^2) time, O(1) space.
public final class Sol {

    public static void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        for (int[] row : matrix) {
            for (int l = 0, r = n - 1; l < r; l++, r--) {
                int tmp = row[l];
                row[l] = row[r];
                row[r] = tmp;
            }
        }
    }

    private Sol() {}
}
