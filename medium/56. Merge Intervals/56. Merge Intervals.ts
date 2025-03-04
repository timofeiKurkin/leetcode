function merge(intervals: number[][]): number[][] {
    const sorted_intervals = intervals.sort((a, b) => a[0] - b[0])
    const res: number[][] = [sorted_intervals[0]]
    let resIndex = 0

    for (let i = 1; i < sorted_intervals.length; i++) {
        const lastRes = res[resIndex]
        if (sorted_intervals[i][0] <= lastRes[1]) {
            res[resIndex] = [res[resIndex][0], Math.max(res[resIndex][1], sorted_intervals[i][1])]
        } else {
            res.push(sorted_intervals[i])
            resIndex += 1
        }
    }

    return res
};