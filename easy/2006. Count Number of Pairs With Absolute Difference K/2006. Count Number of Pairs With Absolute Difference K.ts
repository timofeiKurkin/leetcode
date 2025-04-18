function countKDifference(nums: number[], k: number): number {
    let res = 0
    const n = nums.length

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(nums[j] - nums[i]) === k)
                res += 1
        }
    }

    return res
};