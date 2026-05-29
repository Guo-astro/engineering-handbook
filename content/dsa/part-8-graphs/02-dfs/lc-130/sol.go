// LC 130. Surrounded Regions
package main

func solve(board [][]byte) {
    if len(board) == 0 || len(board[0]) == 0 {
        return
    }
    m, n := len(board), len(board[0])

    var dfs func(r, c int)
    dfs = func(r, c int) {
        if r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O' {
            return
        }
        board[r][c] = '#'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    }

    for r := 0; r < m; r++ {
        dfs(r, 0)
        dfs(r, n-1)
    }
    for c := 0; c < n; c++ {
        dfs(0, c)
        dfs(m-1, c)
    }

    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            switch board[r][c] {
            case 'O':
                board[r][c] = 'X'
            case '#':
                board[r][c] = 'O'
            }
        }
    }
}
