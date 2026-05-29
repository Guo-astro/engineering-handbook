// LC 51. N-Queens (and LC 52. N-Queens II as the count-only sibling)
// runtime tests pass for n in {1, 4, 8, 10}
// (counts: 1, 2, 92, 724 -- matches OEIS A000170).
import java.util.ArrayList;
import java.util.List;

public final class Sol {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> out = new ArrayList<>();
        int[] queens = new int[n];
        backtrack(0, n, 0, 0, 0, queens, out);
        return out;
    }

    public int totalNQueens(int n) {
        return countBacktrack(0, n, 0, 0, 0);
    }

    private void backtrack(int row, int n, int cols, int diag1, int diag2,
                           int[] queens, List<List<String>> out) {
        if (row == n) {
            out.add(buildBoard(queens, n));
            return;
        }
        int available = ((1 << n) - 1) & ~(cols | diag1 | diag2);
        while (available != 0) {
            int bit = available & -available;
            int col = Integer.numberOfTrailingZeros(bit);
            queens[row] = col;
            // Java: use >>> (logical) not >> (arithmetic). Sign-extension
            // would pollute the diag2 mask with phantom attacks.
            backtrack(row + 1, n,
                      cols | bit,
                      (diag1 | bit) << 1,
                      (diag2 | bit) >>> 1,
                      queens, out);
            available &= available - 1;
        }
    }

    private int countBacktrack(int row, int n, int cols, int diag1, int diag2) {
        if (row == n) return 1;
        int total = 0;
        int available = ((1 << n) - 1) & ~(cols | diag1 | diag2);
        while (available != 0) {
            int bit = available & -available;
            total += countBacktrack(row + 1, n,
                                    cols | bit,
                                    (diag1 | bit) << 1,
                                    (diag2 | bit) >>> 1);
            available &= available - 1;
        }
        return total;
    }

    private List<String> buildBoard(int[] queens, int n) {
        List<String> board = new ArrayList<>(n);
        char[] row = new char[n];
        for (int r = 0; r < n; r++) {
            for (int j = 0; j < n; j++) row[j] = '.';
            row[queens[r]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }
}
