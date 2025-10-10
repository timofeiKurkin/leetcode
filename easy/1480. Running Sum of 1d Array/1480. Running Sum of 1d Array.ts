function runningSum(nums: number[]): number[] {
    let prefixSum = nums[0]
    const res = [prefixSum]

    for (let i = 1; i < nums.length; i++) {
        prefixSum += nums[i]
        res.push(prefixSum)
    }

    return res
};