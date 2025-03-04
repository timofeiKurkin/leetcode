function combine(n: number, k: number): number[][] {
    const res: number[][] = []

    const backtracking = (start: number, currPath: number[]): undefined => {
        if (currPath.length === k) {
            res.push(currPath)
            return
        }

        for (let i = start; i < n + 1; i++) {
            currPath.push(i)
            backtracking(i + 1, currPath)
            currPath.pop()
        }
    }

    backtracking(1, [])
    return res
};