function countCompleteSubarrays(nums: number[]): number {
    const totalUnique = (new Set(nums)).size, n = nums.length
    let total = 0, left = 0
    const freq: { [key in number]: number } = {}

    for (let right = 0; right < n; right++) {
        freq[nums[right]] = freq[nums[right]] ? freq[nums[right]] + 1 : 1

        while (Object.keys(freq).length == totalUnique) {
            total += n - right
            freq[nums[left]] -= 1
            if (freq[nums[left]] == 0)
                delete freq[nums[left]]

            left += 1
        }
    }

    return total
};

console.log(countCompleteSubarrays([42]))
console.log(countCompleteSubarrays([1, 2, 3, 4, 5]))
console.log(countCompleteSubarrays([1, 2, 3, 1, 2, 4, 5, 6]))
console.log(countCompleteSubarrays([5, 4, 3, 2, 1, 5, 4, 3, 2, 1]))
console.log(countCompleteSubarrays([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
console.log(countCompleteSubarrays([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]))
console.log(countCompleteSubarrays([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
console.log(countCompleteSubarrays([1, 2, 1, 3, 1, 4, 1, 5, 1]))
console.log(countCompleteSubarrays([1, 1, 2, 2, 3, 3, 4, 4, 5]))
console.log(countCompleteSubarrays([999, 1000, 999, 1000, 999]))
console.log(countCompleteSubarrays([1, 2, 3, 2, 1]))
console.log(countCompleteSubarrays([3, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))


export { }

