function maximumDifference(nums: number[]): number {
    return solution2(nums)
};

function solution1(nums: number[]): number {
    let res = 0
    const n = nums.length

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            res = Math.max(res, nums[j] - nums[i])
        }
    }

    return res || -1
}

function solution2(nums: number[]): number {
    let first = nums[0]
    let diff = 0

    for (const num of nums) {
        if (num < first) {
            first = num
        } else {
            diff = Math.max(diff, num - first)
        }
    }

    return diff || -1
}