function findMin(nums: number[]): number {
    let start = 0

    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            start = i + 1
            break
        }
    }

    return nums[start]
};