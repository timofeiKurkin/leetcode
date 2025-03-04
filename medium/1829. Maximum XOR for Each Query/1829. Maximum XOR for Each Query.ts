function getMaximumXor(nums: number[], maximumBit: number): number[] {

    let k = (1 << maximumBit) - 1
    let xor_sum = 0
    for (const num of nums) {
        xor_sum ^= num
    }

    const items: number[] = []

    for (const item of nums.reverse()) {
        items.push(k ^ xor_sum)
        xor_sum ^= item
    }

    return items
};