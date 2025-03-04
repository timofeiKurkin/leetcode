function threeSum(nums: number[]): number[][] {
    nums = nums.sort((a, b) => a - b)

    const res: number[][] = []

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1])
            continue

        let left = i + 1
        let right = nums.length - 1

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right]

            if (sum > 0)
                right -= 1
            if (sum < 0)
                left += 1
            if (sum === 0) {
                res.push([nums[i], nums[left], nums[right]])

                while (left < right && nums[left] === nums[left + 1])
                    left += 1
                while (left < right && nums[right] === nums[right + 1])
                    right += 1

                left += 1
                right -= 1
            }
        }
    }

    return res
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]))
console.log(threeSum([0, 1, 1]))