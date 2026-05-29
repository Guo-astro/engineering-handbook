// LC 348. Design Tic-Tac-Toe

public class TicTacToe {
    private final int n;
    private final int[] rows;
    private final int[] cols;
    private int diag;
    private int antiDiag;

    public TicTacToe(int n) {
        this.n = n;
        this.rows = new int[n];
        this.cols = new int[n];
        this.diag = 0;
        this.antiDiag = 0;
    }

    public int move(int row, int col, int player) {
        int delta = (player == 1) ? 1 : -1;
        rows[row] += delta;
        cols[col] += delta;
        if (row == col) diag += delta;
        if (row + col == n - 1) antiDiag += delta;

        int target = (player == 1) ? n : -n;
        if (rows[row] == target || cols[col] == target
                || diag == target || antiDiag == target) {
            return player;
        }
        return 0;
    }
}
