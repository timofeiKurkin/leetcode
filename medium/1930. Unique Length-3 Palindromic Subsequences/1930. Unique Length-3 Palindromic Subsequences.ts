function countPalindromicSubsequence(s: string): number {
    const n = s.length
    const first = new Array(26).fill(-1)
    const last = new Array(26).fill(-1)

    for (let i = 0; i < n; i++) {
        const idx = s.charCodeAt(i) - 97
        if (first[idx] === -1) {
            first[idx] = i
        }
        last[idx] = i
    }

    let ans = 0

    for (let i = 0; i < 26; i++) {
        if (first[i] !== -1 && last[i] - first[i] > 1) {
            let mask = 0

            for (let j = first[i] + 1; j < last[i]; j++) {
                mask |= 1 << (s.charCodeAt(j) - 97)
            }

            ans += mask.toString(2).split("1").length - 1
        }
    }

    return ans
};
