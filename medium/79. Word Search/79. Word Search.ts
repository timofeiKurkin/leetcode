function exist(board: string[][], word: string): boolean {
    const t = word.length, m = board.length, n = board[0].length

    const backtrackDFS = (i: number, j: number, index: number): boolean => {
        if (index === t)
            return true

        if (i < 0 || j < 0 || i === m || j === n || board[i][j] !== word[index])
            return false

        const temp = board[i][j]
        board[i][j] = "#"

        const exist = backtrackDFS(i + 1, j, index + 1) || backtrackDFS(i - 1, j, index + 1) || backtrackDFS(i, j + 1, index + 1) || backtrackDFS(i, j - 1, index + 1)

        board[i][j] = temp
        return exist
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === word[0] && backtrackDFS(i, j, 0))
                return true
        }

    }

    return false
};