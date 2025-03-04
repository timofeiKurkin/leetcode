/**
 Do not return anything, modify board in-place instead.
 */
function solve(board: string[][]): void {
    const m = board.length
    const n = board[0].length

    const dfs = (i: number, j: number): void => {
        if (i == m || j == n || i < 0 || j < 0 || board[i][j] == "X")
            return

        if (board[i][j] == "T")
            return

        board[i][j] = "T"

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === "O" && (i === 0 || i === m - 1 || j === 0 || j === n - 1))
                dfs(i, j)
        }
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === "T")
                board[i][j] = "O"
            else if (board[i][j] === "O")
                board[i][j] = "X"
        }
    }
};