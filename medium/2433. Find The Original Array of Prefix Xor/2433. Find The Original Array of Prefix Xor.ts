function findArray(pref: number[]): number[] {
    const n = pref.length
    const res = new Array<number>(n).fill(0)
    res[0] = pref[0]

    for (let i = 1; i < n; i++) {
        res[i] = pref[i - 1] ^ pref[i]
    }

    return res
};