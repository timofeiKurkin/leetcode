function removeDuplicates(nums: number[]): number {
    // let curr = 0, currI = 0
    // for (let i = 0; i <= nums.length; i++) {
    //     if (nums[i] === curr) {
    //         if (currI == 2) {
    //             nums.splice(i, 1)
    //             i -= 1
    //         } else
    //             currI += 1
    //     } else {
    //         curr = nums[i]
    //         currI = 1
    //     }
    // }
    // return nums.length

    let write = 0
    for (let read = 0; read < nums.length; read++) {
        if (write < 2 || nums[read] !== nums[write - 2]) {
            nums[write] = nums[read]
            write++
        }
    }
    return nums.length
};