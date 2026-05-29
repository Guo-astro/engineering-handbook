// LC 348. Design Tic-Tac-Toe

#include <vector>

class TicTacToe {
public:
    TicTacToe(int n) : n_(n), rows_(n, 0), cols_(n, 0), diag_(0), antiDiag_(0) {}

    int move(int row, int col, int player) {
        int delta = (player == 1) ? 1 : -1;
        rows_[row] += delta;
        cols_[col] += delta;
        if (row == col) diag_ += delta;
        if (row + col == n_ - 1) antiDiag_ += delta;

        int target = (player == 1) ? n_ : -n_;
        if (rows_[row] == target || cols_[col] == target
                || diag_ == target || antiDiag_ == target) {
            return player;
        }
        return 0;
    }

private:
    int n_;
    std::vector<int> rows_;
    std::vector<int> cols_;
    int diag_;
    int antiDiag_;
};
