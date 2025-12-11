function maxRepeating(sequence: string, word: string): number {
    let count = 0
    let res = 0

    const n = sequence.length
    const m = word.length

    let i = 0

    for (let i = 0; i < n; i++) {
        let j = i

        while (j <= n - m && sequence.slice(j, j + m) === word) {
            count += 1
            j += m
        }

        res = Math.max(res, count)
        count = 0
    }

    return res
};