function insert(intervals: number[][], newInterval: number[]): number[][] {
    const res: number[][] = []
    let i = 0
    let n = intervals.length

    while (i < n && intervals[i][1] < newInterval[0]) {
        res.push(intervals[i])
        i += 1
    }

    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0])
        newInterval[1] = Math.min(newInterval[1], intervals[i][1])
    }
    res.push(newInterval)

    while (i < n) {
        res.push(intervals[i])
        i += 1
    }

    return res
};