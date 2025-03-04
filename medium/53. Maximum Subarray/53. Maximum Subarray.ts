function maxSubArray(nums: number[]): number {
    let res = -Infinity
    let currSum = 0
    const n = nums.length

    for (let i = 0; i < n; i++) {
        if (currSum < 0) {
            currSum = 0
        }

        currSum = currSum + nums[i]
        res = Math.max(currSum, res)
    }

    return res
};