function maxProduct(nums: number[]): number {
    const n = nums.length
    const dpMin = new Array(n).fill(0)
    const dpMax = new Array(n).fill(0)

    dpMin[0] = dpMax[0] = nums[0]
    let res = nums[0]

    for (let i = 1; i < n; i++) {
        const num = nums[i]
        dpMax[i] = Math.max(num, dpMax[i - 1] * num, dpMin[i - 1] * num)
        dpMin[i] = Math.min(num, dpMax[i - 1] * num, dpMin[i - 1] * num)
        res = Math.max(res, dpMax[i])
    }

    return res
};