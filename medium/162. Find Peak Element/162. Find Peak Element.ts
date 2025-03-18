function findPeakElement(nums: number[]): number {
    if (nums.length === 1)
        return 0

    for (let i = 1; i < nums.length - 1; i++) {
        if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1])
            return i
    }

    return nums[0] > nums[1] ? 0 : nums.length - 1
};