function majorityElement(nums: number[]): number {
    // Boyer-Moore Voting Algorithm
    let candidate = 0
    let count = 0

    for (const num of nums) {
        if (count == 0) {
            candidate = num
        }

        count += candidate === num ? 1 : -1
    }

    return candidate
};