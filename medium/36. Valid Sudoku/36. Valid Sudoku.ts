function isValidSudoku(board: string[][]): boolean {
    const rows: string[][] = Array.from({ length: 9 }, () => [])
    const cols: string[][] = Array.from({ length: 9 }, () => [])
    const blocks: string[][] = Array.from({ length: 9 }, () => [])

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            const num = board[r][c]

            if (num === ".")
                continue

            const block_index = (Math.floor(r / 3)) * 3 + (Math.floor(c / 3))
            if (
                rows[r].includes(num) ||
                cols[c].includes(num) ||
                blocks[block_index].includes(num)
            )
                return false

            rows[r].push(num)
            cols[c].push(num)
            blocks[block_index].push(num)
        }
    }

    return true
};

console.log(Array(9).fill([]))
