function reductionOperations(nums: number[]): number {
    nums.sort((a, b) => b - a)

    let res = 0
    let prevUniqueLargest = nums[0]

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === prevUniqueLargest) continue

        res += i
        prevUniqueLargest = nums[i]
    }

    return res
};