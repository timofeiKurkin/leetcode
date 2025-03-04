function canJump(nums: number[]): boolean {
    const n = nums.length
    let max_reachable = 0

    for (let i = 0; i < n; i++) {
        const step = nums[i]
        if (i > step)
            return false

        max_reachable = Math.max(max_reachable, i + step)

        if (max_reachable >= n - 1)
            return true
    }

    return false
};