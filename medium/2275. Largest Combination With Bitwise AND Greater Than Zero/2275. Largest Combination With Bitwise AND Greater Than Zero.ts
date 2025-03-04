function largestCombination(candidates: number[]): number {
    if (candidates.length == 1) return 1

    let best = 0

    for (let i = 0; i < 24; i++) {
        let count = 0
        for (const num of candidates) {
            count += (num >> i) & 1
        }
        best = Math.max(best, count)
    }

    return best
};