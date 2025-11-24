function prefixesDivBy5(nums: number[]): boolean[] {
    const res: boolean[] = []
    let val = 0

    for (let i = 0; i < nums.length; i++) {
        val = ((val << 1) + nums[i]) % 5
        res[i] = val === 0
    }

    return res
};