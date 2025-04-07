function searchRange(nums: number[], target: number): number[] {
    const first = binarySearch(nums, target, true)
    const second = binarySearch(nums, target, false)
    return [first, second]
};


const binarySearch = (nums: number[], target: number, isFirst: boolean): number => {
    let left = 0, right = nums.length - 1, pos = -1

    while (left <= right) {
        const middle = left + Math.floor((right - left) / 2)
        if (nums[middle] === target) {
            pos = middle
            if (isFirst) {
                right = middle - 1
            } else {
                left = middle + 1
            }
        } else if (nums[middle] < target) {
            left = middle + 1
        } else {
            right = middle - 1
        }
    }

    return pos
}


console.log(searchRange([5, 7, 7, 8, 8, 10], 8))
console.log(searchRange([5, 7, 7, 8, 8, 10], 6))
console.log(searchRange([8, 8], 8))
console.log(searchRange([1], 1))

export { }

