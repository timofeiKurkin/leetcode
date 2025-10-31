function getSneakyNumbers(nums: number[]): number[] {
    const ht = new Set<number>()
    const res: number[] = []

    for (const num of nums) {
        if (ht.has(num)) {
            res.push(num)
        } else {
            ht.add(num)
        }
    }

    return res
};