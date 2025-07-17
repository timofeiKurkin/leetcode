function subarraySum(nums: number[], k: number): number {
    let res = 0
    let currSum = 0
    const ht = new Map<number, number>([[0, 1]])

    for (const num of nums) {
        currSum += num
        const subArray = currSum - k

        res += ht.get(subArray) || 0
        ht.set(currSum, 1 + (ht.get(currSum) || 0))
    }

    return res
};