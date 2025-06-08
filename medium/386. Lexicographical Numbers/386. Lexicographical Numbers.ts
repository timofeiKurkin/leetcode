function lexicalOrder(n: number): number[] {
    const res: number[] = []
    let curr = 1

    for (let i = 0; i < n; i++) {
        res.push(curr)

        if (curr * 10 <= n) {
            curr *= 10
        } else {
            if (curr >= n)
                curr = Math.floor(curr / 10)
            curr += 1
            while (curr % 10 == 0) {
                curr = Math.floor(curr / 10)
            }
        }
    }

    return res
};