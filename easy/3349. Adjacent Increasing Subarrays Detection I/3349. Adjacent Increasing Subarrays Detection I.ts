function hasIncreasingSubarrays(nums: number[], k: number): boolean {
    if (nums.length === 2) {
        return true
    }

    // // {indexes}
    // const set = new Set<number>()
    // let i = 0
    // while (i < nums.length - 1) {
    //     const diff = nums[i + 1] - nums[i]
    //     let start = i
    //     while (i < nums.length - 1 && (nums[i + 1] - nums[i]) === diff) {
    //         i += 1
    //     }
    //     console.log(i, start)
    //     if ((i - start + 1) === k) {
    //         set.add(start)
    //     }
    // }
    // console.log(set)
    // for (const num of set.values()) {
    //     if (set.has(num + k)) {
    //         return true
    //     }
    // }
    // return false

    // let a = 0, b = 1
    // while (a < nums.length - 1) {
    //     const diff = nums[a + 1] - nums[a]
    //     const startA = a
    //     while (a < nums.length - 1 && nums[a + 1] - nums[a] === diff) {
    //         a += 1
    //     }
    //     if (a < nums.length - 1 && (a - startA + 1) === k) {
    //         b = a + 1
    //         const diffB = nums[b + 1] - nums[b]
    //         const startB = b
    //         while (b < nums.length - 1 && nums[b + 1] - nums[b] === diffB) {
    //             b += 1
    //         }
    //         if ((b - startB + 1) === k) {
    //             return true
    //         }
    //     }
    // }
    // return false

    const n = nums.length
    let len = 1, prev = 0

    for (let i = 1; i < n && Math.max(Math.floor(len / 2), Math.min(len, prev)) < k; i++) {
        if (nums[i] > nums[i - 1]) {
            len += 1
        } else {
            prev = len
            len = 1
        }
    }

    return Math.max(Math.floor(len / 2), Math.min(len, prev)) >= k
};