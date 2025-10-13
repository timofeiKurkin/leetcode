function binarySearch(nums: number[]) {
    let left = 0, right = nums.length - 1

    while (left <= right) {
        const middle = Math.floor((right + left) / 2)

        if (nums[middle] >= 0) {
            left = middle + 1
        } else {
            right = middle - 1
        }

    }

    return left
}

function countNegatives(grid: number[][]): number {
    let res = 0

    for (const nums of grid) {
        const left = binarySearch(nums)
        console.log(left)

        res += (nums.length - left)
    }

    return res
};