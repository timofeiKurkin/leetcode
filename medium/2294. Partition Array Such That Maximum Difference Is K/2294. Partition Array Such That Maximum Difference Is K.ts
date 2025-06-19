function partitionArray(nums: number[], k: number): number {
    nums.sort((a, b) => a - b)

    let res = 1, prev = nums[0]
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] - prev > k) {
            prev = nums[i]
            res += 1
        }
    }
    return res
};