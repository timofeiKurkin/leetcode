function generateParenthesis(n: number): string[] {
    const res: string[] = []
    const o = "(", c = ")"

    const backtrack = (path: string, opened: number, closed: number) => {
        if (path.length === n * 2) {
            res.push(path)
            return
        }

        if (opened < n)
            backtrack(path + o, opened + 1, closed)

        if (closed < opened)
            backtrack(path + c, opened, closed + 1)

        return
    }

    backtrack("", 0, 0)

    return res
};