// 26. Remove Duplicates from Sorted Array
// Дано: 

function removeDuplicates(nums: number[]): number {
    // for (let i = 0; i < nums.length; i++) {
    //     if (nums[i] === nums[i + 1]) {
    //         nums.splice(i, 1)
    //         i -= 1
    //     }
    // }

    // return nums.length

    if (!nums.length) return 0

    let uniqueIndex = 0

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== nums[uniqueIndex]) {
            uniqueIndex++
            nums[uniqueIndex] = nums[i]
        }
    }

    return uniqueIndex + 1
};

console.log(removeDuplicates([1, 1, 2]))
console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))