function maxSubarraySumCircular(nums: number[]): number {
    const kadane = (arr: number[]) => {
        let res = arr[0]
        let maxRes = arr[0]

        for (const num of arr.slice(1,)) {
            maxRes = maxRes + num
            res = Math.max(maxRes, res)
        }

        return res
    }

    const normalSubarraySum = kadane(nums)

    if (normalSubarraySum < 0)
        return normalSubarraySum

    const totalSum = nums.reduce((acc, curr) => acc + curr, 0)
    const invertNums = nums.map((item) => -item)
    const invertNumsSum = kadane(invertNums)
    const minimumSubarraySum = totalSum + invertNumsSum

    return Math.max(normalSubarraySum, minimumSubarraySum)
};