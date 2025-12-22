function waysToMakeFair(nums: number[]): number {
    let evenSum = 0
    let oddSum = 0

    for (let j = 0; j < nums.length; j++) {
        if (j % 2 === 0) oddSum += nums[j]
        else evenSum += nums[j]
    }

    let res = 0
    let prefixEvenSum = 0, prefixOddSum = 0

    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) evenSum -= nums[i]
        else oddSum -= nums[i]

        const updatedEven = prefixEvenSum + oddSum
        const updatedOdd = prefixOddSum + evenSum

        if (updatedEven === updatedOdd) res += 1
        if (i % 2 === 0) prefixEvenSum += nums[i]
        else prefixOddSum += nums[i]
    }

    return res
};