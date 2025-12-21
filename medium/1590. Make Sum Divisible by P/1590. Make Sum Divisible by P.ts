function sum(nums: number[]) {
    return nums.reduce((acc, curr) => acc += curr)
}

function minSubarray(nums: number[], p: number): number {
    const n = nums.length
    const modP = sum(nums) % p

    if (modP === 0) return 0

    const ht: Record<number, number> = { 0: -1 }
    let prefixSum = 0, length = n

    for (let i = 0; i < n; i++) {
        const num = nums[i]
        prefixSum = (prefixSum + num) % p
        const prefixToRemove = (prefixSum - modP + p) % p

        if (prefixToRemove in ht) {
            length = Math.min(length, i - ht[prefixToRemove])
        }

        ht[prefixSum] = i
    }

    return length === n ? -1 : length
};