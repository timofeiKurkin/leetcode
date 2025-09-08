function maximumStrongPairXor(nums: number[]): number {
    return solution2(nums)
};

function solution1(nums: number[]): number {
    nums.sort()
    let maxStrongPair = 0

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            const x = nums[i], y = nums[j]
            if (Math.abs(x - y) <= Math.min(x, y)) {
                maxStrongPair = Math.max(maxStrongPair, x ^ y)
            }
        }
    }

    return maxStrongPair
}