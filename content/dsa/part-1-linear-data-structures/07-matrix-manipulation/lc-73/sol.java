// LC 73. Set Matrix Zeroes
// In place, O(1) extra space. Use row 0 and column 0 as the marker arrays;
// two booleans capture whether row 0 or column 0 originally contained a
// zero (the marker pass overwrites cell (0, 0) and loses that information).
// Read the flags BEFORE the marker pass — that ordering is the bug fix.
// O(m*n) time, O(1) extra space.
public final class Sol {

    public static void setZeroes(int[][] matrix) {
        int m = matrix.length;
        if (m == 0) return;
        int n = matrix[0].length;
        if (n == 0) return;
        boolean firstRowHasZero = false, firstColHasZero = false;
        for (int j = 0; j < n; j++) if (matrix[0][j] == 0) { firstRowHasZero = true; break; }
        for (int i = 0; i < m; i++) if (matrix[i][0] == 0) { firstColHasZero = true; break; }
        // Pass 1: mark dirty rows/cols via row 0 and col 0.
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        // Pass 2: apply marks to the inner region.
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
            }
        }
        // Pass 3: zero row 0 / col 0 themselves if they were originally dirty.
        if (firstRowHasZero) for (int j = 0; j < n; j++) matrix[0][j] = 0;
        if (firstColHasZero) for (int i = 0; i < m; i++) matrix[i][0] = 0;
    }

    private Sol() {}
}
