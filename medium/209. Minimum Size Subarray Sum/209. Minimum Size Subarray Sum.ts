function minSubArrayLen(target: number, nums: number[]): number {
    const n = nums.length
    let min_length = Infinity
    let window_sum = 0
    let left = 0

    for (let right = 0; right < n; right++) {
        window_sum += nums[right]

        while (window_sum >= target) {
            min_length = Math.min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
        }
    }

    return min_length !== Infinity ? min_length : 0
};

console.log(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
console.log(minSubArrayLen(4, [1, 4, 4]))
console.log(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
console.log(minSubArrayLen(11, [1, 2, 3, 4, 5]))