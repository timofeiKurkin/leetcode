function maxSubsequence(nums: number[], k: number): number[] {
    const n = nums.length
    let newNums = nums.map((n, i) => [n, i])
    newNums.sort((a, b) => a[0] - b[0])
    newNums = newNums.slice(n - k,)
    newNums.sort((a, b) => a[1] - b[1])
    return newNums.map((arr) => arr[0])
};