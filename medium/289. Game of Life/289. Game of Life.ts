/**
 Do not return anything, modify board in-place instead.
 */
function gameOfLife(board: number[][]): void {

    const m = board.length
    const n = board[0].length

    const directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1],
    ]

    for (let i = 0; i <= m; i++) {
        for (let j = 0; j <= n; j++) {
            let live_neighbors = 0

            for (const [di, dj] of directions) {
                let ni = i + di
                let nj = j + dj

                const ni_cond = 0 <= ni && ni < m
                const nj_cond = 0 <= nj && nj < n

                if (ni_cond && nj_cond && Math.abs(board[ni][nj]) === 1) {
                    live_neighbors += 1
                }
            }

            if (board[i][j] === 1 && (live_neighbors < 2 || live_neighbors > 3)) {
                board[i][j] = -1
            } else if (board[i][j] === 0 && live_neighbors === 3) {
                board[i][j] = 2
            }

        }
    }

    for (let i = 0; i <= m; i++) {
        for (let j = 0; j <= n; j++) {
            if (board[i][j] === -1) {
                board[i][j] = 0
            } else if (board[i][j] === 2) {
                board[i][j] = 1
            }
        }
    }

};