function findLHS(nums: number[]): number {
    nums.sort((a, b) => a - b)

    let maxLength = 0
    let left = 0, right = 1

    while (right < nums.length) {
        const difference = Math.abs(nums[left] - nums[right])

        if (difference === 0) {
            right += 1
        } else if (difference > 1) {
            left += 1

            if (left === right) {
                right += 1
            }
        } else {
            maxLength = Math.max(maxLength, right - left + 1)
            right += 1
        }
    }

    return maxLength
};
