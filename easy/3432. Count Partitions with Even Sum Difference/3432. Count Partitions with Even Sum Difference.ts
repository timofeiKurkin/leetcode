function sum(nums: number[]) {
    return nums.reduce((curr, acc) => curr += acc)
}

function countPartitions(nums: number[]): number {
    let prefixSum = nums[0]
    let totalSum = sum(nums) - nums[0]

    let res = 0

    for (let i = 1; i < nums.length; i++) {
        if (!(Math.abs(prefixSum - totalSum) % 2)) res += 1
        prefixSum += nums[i]
        totalSum -= nums[i]
    }

    return res
};