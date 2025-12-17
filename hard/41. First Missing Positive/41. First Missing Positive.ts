function firstMissingPositive(nums: number[]): number {
    // nums.push(0)
    // const n = nums.length
    // for (let i = 0; i < n; i++) {
    //     if (nums[i] < 0 || nums[i] >= n)
    //         nums[i] = 0
    // }
    // for (let i = 0; i < n; i++) {
    //     nums[nums[i] % n] += n
    // }
    // for (let i = 1; i < n; i++) {
    //     if (!(nums[i] / n)) return i
    // }
    // return n

    nums.sort((a, b) => a - b)

    let missing = 1

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0 && nums[i] === missing) missing += 1
        else if (nums[i] > missing) return missing
    }

    return missing
};
