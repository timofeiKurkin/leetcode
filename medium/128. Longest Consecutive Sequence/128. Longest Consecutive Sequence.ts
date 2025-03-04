function longestConsecutive(nums: number[]): number {
    if (!nums.length)
        return 0

    const numSet = new Set(nums)
    let maxLength = 0

    for (const num of numSet) {
        if (!(numSet.has(num - 1))) {
            let currentNum = num
            let currentLength = 1

            while (numSet.has(currentNum + 1)) {
                currentNum += 1
                currentLength += 1
            }

            maxLength = Math.max(maxLength, currentLength)
        }
    }

    return maxLength
}

console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))