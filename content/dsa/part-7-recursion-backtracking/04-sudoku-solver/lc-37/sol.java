// LC 37. Sudoku Solver
public final class Sol {
    private char[][] board;
    private final int[] rows = new int[9];
    private final int[] cols = new int[9];
    private final int[] boxes = new int[9];

    private static int boxIndex(int r, int c) { return (r / 3) * 3 + (c / 3); }

    public void solveSudoku(char[][] board) {
        this.board = board;
        final int ALL = 0x1FF;
        for (int i = 0; i < 9; i++) { rows[i] = cols[i] = boxes[i] = ALL; }
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] != '.') {
                    int bit = 1 << (board[r][c] - '1');
                    rows[r] ^= bit;
                    cols[c] ^= bit;
                    boxes[boxIndex(r, c)] ^= bit;
                }
            }
        }
        backtrack();
    }

    private boolean backtrack() {
        int bestR = -1, bestC = -1, bestCount = 10, bestMask = 0;
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] != '.') continue;
                int cand = rows[r] & cols[c] & boxes[boxIndex(r, c)];
                int count = Integer.bitCount(cand);
                if (count < bestCount) {
                    bestCount = count; bestR = r; bestC = c; bestMask = cand;
                    if (count <= 1) break;
                }
            }
            if (bestCount <= 1) break;
        }
        if (bestR == -1) return true;
        if (bestCount == 0) return false;

        int r = bestR, c = bestC, b = boxIndex(r, c), cand = bestMask;
        while (cand != 0) {
            int bit = cand & -cand;
            cand ^= bit;
            int d = Integer.numberOfTrailingZeros(bit) + 1;
            board[r][c] = (char) ('0' + d);
            rows[r] ^= bit;
            cols[c] ^= bit;
            boxes[b] ^= bit;
            if (backtrack()) return true;
            rows[r] ^= bit;
            cols[c] ^= bit;
            boxes[b] ^= bit;
            board[r][c] = '.';
        }
        return false;
    }
}
