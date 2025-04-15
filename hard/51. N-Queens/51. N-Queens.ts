function solveNQueens(n: number): string[][] {
    const col = new Set()
    const positiveDiag = new Set() // (r + c)
    const negativeDiag = new Set() // (r - c)

    const res: string[][] = []
    const board = Array.from({ length: n }, (): string[] => new Array(n).fill("."))

    const backtrack = (r: number): void => {
        if (r === n) {
            const finalBoard = Array.from({ length: n }, (_, i): string => board[i].join(""))
            res.push(finalBoard)
            return
        }

        for (let c = 0; c < n; c++) {
            if (col.has(c) || positiveDiag.has(r + c) || negativeDiag.has(r - c))
                continue

            col.add(c)
            positiveDiag.add(r + c)
            negativeDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.delete(c)
            positiveDiag.delete(r + c)
            negativeDiag.delete(r - c)
            board[r][c] = "."
        }
    }

    backtrack(0)
    return res
};

console.log(solveNQueens(4))

export { }

