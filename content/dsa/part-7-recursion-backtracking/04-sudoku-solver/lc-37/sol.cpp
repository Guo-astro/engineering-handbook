// LC 37. Sudoku Solver
#include <vector>
#include <bitset>

class Solution {
public:
    void solveSudoku(std::vector<std::vector<char>>& board) {
        board_ = &board;
        const int ALL = 0x1FF;
        for (int i = 0; i < 9; ++i) rows_[i] = cols_[i] = boxes_[i] = ALL;
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] != '.') {
                    int bit = 1 << (board[r][c] - '1');
                    rows_[r] ^= bit;
                    cols_[c] ^= bit;
                    boxes_[boxIndex(r, c)] ^= bit;
                }
            }
        }
        backtrack();
    }

private:
    std::vector<std::vector<char>>* board_;
    int rows_[9], cols_[9], boxes_[9];
    static int boxIndex(int r, int c) { return (r / 3) * 3 + (c / 3); }

    bool backtrack() {
        int bestR = -1, bestC = -1, bestCount = 10, bestMask = 0;
        auto& b = *board_;
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (b[r][c] != '.') continue;
                int cand = rows_[r] & cols_[c] & boxes_[boxIndex(r, c)];
                int count = std::bitset<9>(cand).count();
                if (count < bestCount) {
                    bestCount = count; bestR = r; bestC = c; bestMask = cand;
                    if (count <= 1) break;
                }
            }
            if (bestCount <= 1) break;
        }
        if (bestR == -1) return true;
        if (bestCount == 0) return false;

        int r = bestR, c = bestC, bx = boxIndex(r, c), cand = bestMask;
        while (cand != 0) {
            int bit = cand & -cand;
            cand ^= bit;
            int d = __builtin_ctz(bit) + 1;
            b[r][c] = static_cast<char>('0' + d);
            rows_[r] ^= bit;
            cols_[c] ^= bit;
            boxes_[bx] ^= bit;
            if (backtrack()) return true;
            rows_[r] ^= bit;
            cols_[c] ^= bit;
            boxes_[bx] ^= bit;
            b[r][c] = '.';
        }
        return false;
    }
};
