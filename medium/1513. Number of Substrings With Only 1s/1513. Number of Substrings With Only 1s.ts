function numSub(s: string): number {
    let res = 0
    let i = 0

    while (i < s.length) {
        let j = i

        if (s[i] === "0") {
            i += 1
        } else {
            while (s[j] === "1") {
                j += 1
            }

            const n = j - i
            res += n * (n + 1) / 2
            i = j
        }
    }

    return res % (10 ** 9 + 7)
};