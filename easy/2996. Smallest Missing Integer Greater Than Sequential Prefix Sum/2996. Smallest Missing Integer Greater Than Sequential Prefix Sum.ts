function missingInteger(nums: number[]): number {
    const items = new Set(nums)
    let prefixSum = nums[0]

    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] + 1 === nums[i]) {
            prefixSum += nums[i]
        } else {
            break
        }
    }

    while (items.has(prefixSum)) {
        prefixSum += 1
    }

    return prefixSum
};