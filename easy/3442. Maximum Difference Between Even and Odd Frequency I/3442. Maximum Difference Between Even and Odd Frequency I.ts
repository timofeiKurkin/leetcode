function maxDifference(s: string): number {
    const cnt: { [key in string]: number } = {}
    for (const c of s) {
        cnt[c] = !cnt[c] ? 1 : cnt[c] + 1
    }
    console.log(cnt)

    let maxOdd = 0
    let minEven = 10 ** 10

    for (const v of Object.values(cnt)) {
        if (v % 2 !== 0) {
            maxOdd = Math.max(maxOdd, v)
        } else {
            minEven = Math.min(minEven, v)
        }
    }

    return maxOdd - minEven
};