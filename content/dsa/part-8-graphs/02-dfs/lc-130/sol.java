// LC 130. Surrounded Regions
public class Sol {
    public static void solve(char[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) return;
        int m = board.length, n = board[0].length;
        for (int r = 0; r < m; r++) {
            dfs(board, r, 0, m, n);
            dfs(board, r, n - 1, m, n);
        }
        for (int c = 0; c < n; c++) {
            dfs(board, 0, c, m, n);
            dfs(board, m - 1, c, m, n);
        }
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == '#') board[r][c] = 'O';
            }
        }
    }

    private static void dfs(char[][] b, int r, int c, int m, int n) {
        if (r < 0 || r >= m || c < 0 || c >= n || b[r][c] != 'O') return;
        b[r][c] = '#';
        dfs(b, r + 1, c, m, n);
        dfs(b, r - 1, c, m, n);
        dfs(b, r, c + 1, m, n);
        dfs(b, r, c - 1, m, n);
    }
}
