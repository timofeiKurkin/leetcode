function createDiapason(a: number, b: number) {
    return a != b ? `${a}->${b}` : a.toString()
}

function summaryRanges(nums: number[]): string[] {
    if (!nums.length)
        return []


    const res: string[] = []
    let start: number[] = [nums[0]]

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] != nums[i - 1] + 1) {
            res.push(createDiapason(start[0], nums[i - 1]))
            start = [nums[i]]
        }
    }

    if (start.length) {
        res.push(createDiapason(start[0], nums.slice(-1)[0]))
    }

    return res
};

console.log(summaryRanges([0, 1, 2, 4, 5, 7]))
console.log(summaryRanges([0, 2, 3, 4, 6, 8, 9]))