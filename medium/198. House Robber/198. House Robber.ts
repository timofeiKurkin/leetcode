function rob(nums: number[]): number {
    if (!nums.length)
        return 0
    if (nums.length === 1)
        return nums[0]

    let prev1 = 0
    let prev2 = nums[0]

    for (let i = 1; i < nums.length; i++) {
        const max_rob = Math.max(prev2, prev1 + nums[i])
        prev1 = prev2
        prev2 = max_rob
    }

    return prev2
};