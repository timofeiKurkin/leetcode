function findMaxConsecutiveOnes(nums: number[]): number {
    let res = 0
    let i = 0

    while (i < nums.length) {
        if (nums[i] === 1) {
            let j = i + 1

            while (nums[j] === 1) {
                j += 1
            }

            res = Math.max(res, j - i)
            i = j + 1
        } else {
            i += 1
        }
    }

    return res
};