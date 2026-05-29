// LC 51. N-Queens (and LC 52. N-Queens II as the count-only sibling)
// runtime tests pass for n in {1, 4, 8, 10}
// (counts: 1, 2, 92, 724 -- matches OEIS A000170).
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::vector<std::string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> out;
        std::vector<int> queens(n, -1);
        backtrack(0, n, 0, 0, 0, queens, out);
        return out;
    }

    int totalNQueens(int n) {
        return countBacktrack(0, n, 0, 0, 0);
    }

private:
    void backtrack(int row, int n, int cols, int diag1, int diag2,
                   std::vector<int>& queens,
                   std::vector<std::vector<std::string>>& out) {
        if (row == n) {
            std::vector<std::string> board;
            board.reserve(n);
            for (int r = 0; r < n; ++r) {
                std::string line(n, '.');
                line[queens[r]] = 'Q';
                board.push_back(std::move(line));
            }
            out.push_back(std::move(board));
            return;
        }
        int available = ((1 << n) - 1) & ~(cols | diag1 | diag2);
        while (available) {
            int bit = available & -available;
            int col = __builtin_ctz(bit);                // count trailing zeros
            queens[row] = col;
            backtrack(row + 1, n,
                      cols  | bit,
                      (diag1 | bit) << 1,
                      (diag2 | bit) >> 1,
                      queens, out);
            available &= available - 1;
        }
    }

    int countBacktrack(int row, int n, int cols, int diag1, int diag2) {
        if (row == n) return 1;
        int total = 0;
        int available = ((1 << n) - 1) & ~(cols | diag1 | diag2);
        while (available) {
            int bit = available & -available;
            total += countBacktrack(row + 1, n,
                                    cols  | bit,
                                    (diag1 | bit) << 1,
                                    (diag2 | bit) >> 1);
            available &= available - 1;
        }
        return total;
    }
};
