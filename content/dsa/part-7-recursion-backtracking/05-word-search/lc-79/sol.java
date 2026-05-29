// LC 79. Word Search
public final class Sol {
    public boolean exist(char[][] board, String word) {
        if (board == null || board.length == 0 || board[0].length == 0
                || word == null || word.isEmpty()) {
            return false;
        }
        int rows = board.length;
        int cols = board[0].length;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == word.charAt(0) && dfs(board, r, c, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int r, int c, int k, String word) {
        if (k == word.length()) return true;
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length
                || board[r][c] != word.charAt(k)) {
            return false;
        }
        char saved = board[r][c];
        board[r][c] = '#';   // sentinel never matches a real word char (LC 79: letters only)
        boolean found = dfs(board, r + 1, c, k + 1, word)
                     || dfs(board, r - 1, c, k + 1, word)
                     || dfs(board, r, c + 1, k + 1, word)
                     || dfs(board, r, c - 1, k + 1, word);
        board[r][c] = saved; // restore on backtrack
        return found;
    }
}
