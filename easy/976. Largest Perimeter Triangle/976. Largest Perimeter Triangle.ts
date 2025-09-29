function largestPerimeter(nums: number[]): number {
    return solution2(nums)
};

function solution1(nums: number[]): number {
    nums.sort((a, b) => b - a)
    const n = nums.length

    for (let i = 0; i < n; i++) {
        const x1 = nums[i]

        for (let j = i + 1; j < n; j++) {
            const x2 = nums[j]

            for (let k = j + 1; k < n; k++) {
                const x3 = nums[k]

                if ((x3 + x2) > x1) {
                    return x1 + x2 + x3
                }
            }
        }
    }

    return 0
}

function solution2(nums: number[]): number {
    nums.sort((a, b) => b - a)
    for (let i = 0; i < nums.length - 2; i++) {
        if ((nums[i + 1] + nums[i + 2]) > nums[i]) {
            return nums[i] + nums[i + 1] + nums[i + 2]
        }
    }
    return 0
}