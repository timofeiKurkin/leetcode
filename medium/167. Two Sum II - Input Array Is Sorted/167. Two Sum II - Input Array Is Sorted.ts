function twoSum(numbers: number[], target: number): number[] {
    const seen = new Map()

    for (const [i, num] of numbers.entries()) {
        const exactDiff = target - num


        if (seen.has(exactDiff)) {
            return [seen.get(exactDiff), i + 1]
        }

        if (!seen.has(num)) {
            seen.set(num, i + 1)
        }
    }

    return []
};