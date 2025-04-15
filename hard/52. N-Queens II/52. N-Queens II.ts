function totalNQueens(n: number): number {
    const col = new Set()
    const positiveDiag = new Set() // (r + c)
    const negativeDiag = new Set() // (r - c)

    let res: number = 0

    const backtrack = (r: number): void => {
        if (r === n) {
            res += 1
            return
        }

        for (let c = 0; c < n; c++) {
            if (col.has(c) || positiveDiag.has(r + c) || negativeDiag.has(r - c))
                continue

            col.add(c)
            positiveDiag.add(r + c)
            negativeDiag.add(r - c)

            backtrack(r + 1)

            col.delete(c)
            positiveDiag.delete(r + c)
            negativeDiag.delete(r - c)
        }
    }

    backtrack(0)
    return res
};