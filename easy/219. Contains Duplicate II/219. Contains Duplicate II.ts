function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const seen = new Map()

    for (let i = 0; i <= nums.length; i++) {
        if (seen.has(nums[i])) {
            const j = seen.get(nums[i])
            if (Math.abs(i - j) <= k)
                return true
        }
        seen.set(nums[i], i)
    }

    return false
};