function maxFrequencyElements(nums: number[]): number {
    const ht = new Map<number, number>()

    for (const num of nums) {
        ht.set(num, (ht.get(num) || 0) + 1)
    }

    let frequency = 0, count = 0

    for (const [_, freq] of ht) {
        if (freq > frequency) {
            frequency = freq
            count = freq
        } else if (freq === frequency) {
            count += freq
        }
    }

    return frequency * count
};