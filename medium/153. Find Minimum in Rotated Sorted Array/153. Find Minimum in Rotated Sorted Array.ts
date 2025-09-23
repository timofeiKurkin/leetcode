function findMin(nums: number[]): number {
    return solution2(nums)
};

function solution1(nums: number[]): number {
    // TIME: O(N)

    let start = 0

    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            start = i + 1
            break
        }
    }

    return nums[start]
}

function solution2(nums: number[]): number {
    // TIME: O(log N)

    const n = nums.length
    let low = 0, high = n - 1
    let res = 0

    while (low <= high) {
        const middle = low + Math.floor((high - low) / 2)

        if (nums[middle] <= nums[n - 1]) {
            res = middle
            high = middle - 1
        } else {
            low = middle + 1
        }
    }

    return nums[res]
}