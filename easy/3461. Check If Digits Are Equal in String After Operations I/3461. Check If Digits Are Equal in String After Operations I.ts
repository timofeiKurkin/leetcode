function hasSameDigits(s: string): boolean {
    const nums = s.split("").map((i) => Number(i))
    let end = nums.length - 1

    while (end > 1) {
        for (let i = 0; i < end; i++) {
            nums[i] = (nums[i] + nums[i + 1]) % 10
        }
        end -= 1
    }

    return nums[0] === nums[1]
};