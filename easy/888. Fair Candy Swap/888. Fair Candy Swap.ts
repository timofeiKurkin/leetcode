function sum(nums: number[]) {
    return nums.reduce((acc, curr) => curr + acc, 0)
}

function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {
    const diff = Math.floor((sum(aliceSizes) - sum(bobSizes)) / 2)
    const aliceSet = new Set(aliceSizes)

    for (const bobSize of new Set(bobSizes)) {
        if (aliceSet.has(diff + bobSize)) {
            return [diff + bobSize, bobSize]
        }
    }

    return []
};