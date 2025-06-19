function divideArray(nums: number[], k: number): number[][] {
    nums.sort((a, b) => a - b)

    const n = nums.length
    const res: number[][] = []

    for (let i = 0; i <= n - 2; i += 3) {
        if (nums[i + 2] - nums[i] > k) return []
        res.push(nums.slice(i, i + 3))
    }

    return res
};